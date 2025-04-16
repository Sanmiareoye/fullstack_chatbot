from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.openai_helpers import chat_helper
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class ChatInput(BaseModel):
    userInput: str

@router.post("/sendText")
async def send_text(chat_input: ChatInput):
    logger.debug(f"/sendText - Recieved input: {chat_input.userInput}")
    message = {"role":"user", "content": chat_input.userInput}
    try:
        result = await chat_helper(message)
        logger.debug(f"/sendText - Returning result: {result}")
        return JSONResponse(content=result)
    except Exception as e:
        logger.error(f"/sendText - Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))