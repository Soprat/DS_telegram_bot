from aiogram.types import Message
from aiogram.enums import MessageEntityType
from typing import Any, Union


def mention_filter(message: Message) -> Union[bool, dict[str, Any]]:
    """
    Use this filter to extract the first mention_filter entity from message.
    :return: A dictionary that'll update handling context.
    """
    for entity in message.entities:
        if entity.type == MessageEntityType.MENTION:
            return {"mention_filter": entity}
    return False
