import logging
from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable


class LoggingMiddleware(BaseMiddleware):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:
        username = data['event_context'].chat.username \
            if data['event_context'].chat.username else data['event_context'].chat.id
        self.logger.info(f"{username} triggered: {data['event_router'].name}")
        return await handler(event, data)
