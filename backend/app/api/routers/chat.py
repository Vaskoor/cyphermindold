"""RAG chat router."""
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
from app.services.rag_service import rag_service
import asyncio, json

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    history: Optional[list[dict]] = None

@router.post("")
async def chat(body: ChatRequest):
    answer = await rag_service.query_with_llm(body.message, body.history)
    chunks = rag_service.retrieve(body.message, top_k=3)
    return {
        "answer": answer,
        "citations": [{"content": c.content[:300], "score": c.score} for c in chunks],
    }
