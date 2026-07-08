"""NVIDIA NIM / integrate.api.nvidia.com chat completions client."""
from __future__ import annotations

import logging
from typing import Optional

import httpx

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class LLMError(Exception):
    """Raised when the LLM API call fails."""


async def chat_completion(
    messages: list[dict[str, str]],
    *,
    temperature: float = 0.7,
    max_tokens: int = 4096,
    top_p: float = 1.0,
    model: Optional[str] = None,
) -> str:
    """
    Call NVIDIA chat completions API (OpenAI-compatible).

    Parameters
    ----------
    messages : list of {"role": "system"|"user"|"assistant", "content": str}

    Returns
    -------
    Assistant response text.
    """
    api_key = settings.nvidia_api_key
    if not api_key:
        raise LLMError(
            "NVIDIA_API_KEY is not set. Add it to your .env file."
        )

    payload = {
        "model": model or settings.llm_model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stream": False,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    url = f"{settings.nvidia_api_base.rstrip('/')}/chat/completions"

    async with httpx.AsyncClient(timeout=settings.llm_timeout_seconds) as client:
        try:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
        except httpx.HTTPStatusError as exc:
            detail = exc.response.text[:500]
            logger.error("NVIDIA API error %s: %s", exc.response.status_code, detail)
            raise LLMError(f"NVIDIA API error {exc.response.status_code}: {detail}") from exc
        except httpx.RequestError as exc:
            logger.error("NVIDIA API request failed: %s", exc)
            raise LLMError(f"NVIDIA API unreachable: {exc}") from exc

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise LLMError(f"Unexpected NVIDIA API response: {data}") from exc


async def check_llm_health() -> dict:
    """Ping NVIDIA API with a minimal completion."""
    if not settings.nvidia_api_key:
        return {"online": False, "models": [], "provider": "nvidia", "error": "API key not configured"}

    try:
        reply = await chat_completion(
            [{"role": "user", "content": "Reply with exactly: ok"}],
            temperature=0,
            max_tokens=8,
        )
        return {
            "online": True,
            "models": [settings.llm_model],
            "provider": "nvidia",
            "version": settings.nvidia_api_base,
            "test_reply": reply.strip()[:32],
        }
    except LLMError as exc:
        return {"online": False, "models": [settings.llm_model], "provider": "nvidia", "error": str(exc)}
