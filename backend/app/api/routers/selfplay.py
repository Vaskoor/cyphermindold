"""Self-play arena router."""
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from datetime import datetime
from app.db.base import get_db
from app.models.selfplay import SelfPlayGame, SelfPlayMove
from app.services.selfplay_service import run_selfplay_game

router = APIRouter(prefix="/selfplay", tags=["selfplay"])

class SelfPlayRequest(BaseModel):
    target_code: str
    language: str = "python"
    max_rounds: int = 5

@router.post("/start")
async def start_selfplay(body: SelfPlayRequest, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    game = SelfPlayGame(
        target_code=body.target_code[:10000],
        target_language=body.language,
        status="running",
    )
    db.add(game)
    await db.commit()
    await db.refresh(game)

    async def run_and_save():
        result = await run_selfplay_game(body.target_code, body.language, body.max_rounds)
        game.status = "completed"
        game.winner = result["winner"]
        game.total_rounds = result["total_rounds"]
        game.novel_patterns_found = result["novel_patterns_found"]
        game.completed_at = datetime.utcnow()
        for r in result["rounds"]:
            db.add(SelfPlayMove(
                game_id=game.id,
                round_number=r["round"],
                team="red",
                move_type="attack",
                content=r["red_move"],
                is_novel=r["is_novel"],
            ))
            db.add(SelfPlayMove(
                game_id=game.id,
                round_number=r["round"],
                team="blue",
                move_type="defense",
                content=r["blue_move"],
            ))
        await db.commit()

    background_tasks.add_task(run_and_save)
    return {"game_id": game.id, "status": "started"}

@router.get("/status/{game_id}")
async def game_status(game_id: int, db: AsyncSession = Depends(get_db)):
    from sqlalchemy import select
    result = await db.execute(select(SelfPlayGame).where(SelfPlayGame.id == game_id))
    game = result.scalar_one_or_none()
    if not game:
        from fastapi import HTTPException
        raise HTTPException(404, "Game not found")
    return {
        "id": game.id,
        "status": game.status,
        "winner": game.winner,
        "total_rounds": game.total_rounds,
        "novel_patterns_found": game.novel_patterns_found,
    }
