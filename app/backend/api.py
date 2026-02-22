from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

from app.config.settings import settings
from app.core.ai_agent import get_response_from_ai_agents
from app.common.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Multi AI Agent")


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[Dict[str, str]]
    allow_search: bool


@app.post("/chat")
async def chat_endpoint(request: RequestState):

    logger.info(f"Received request for model: {request.model_name}")

    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        raise HTTPException(
            status_code=400,
            detail="Invalid model name"
        )

    if not request.messages:
        raise HTTPException(
            status_code=400,
            detail="Messages cannot be empty"
        )

    try:
        response = get_response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )

        return {"response": response}

    except Exception as e:
        logger.exception("Error during AI response generation")
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )