import logging
from typing import List, Dict
from fastapi import HTTPException
from config import client

logger = logging.getLogger(__name__)

async def chat_helper(message: Dict, model:str = "gpt-4",
                      system_configuration: str = "You are a helpful assistant.",
                      message_history: List[Dict] = []):
    messages = [{"role": "system", "content": system_configuration}] + message_history + [message]
    logger.debug(f"chat_helper - Sending messages: {messages}")
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages
        )

        logger.debug(f"chat_helper - Received completion: {completion}")
        response_message = {
            "role" :"assistant",
            "content" : completion.choices[0].message.content,
            "refusal" : None
        }
        return response_message
    except Exception as e:
        logger.error(f"chat_helper - Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))