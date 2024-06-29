import re
import data
from main import bot
from aiogram.types import (Message,
                           MessageEntity,
                           CallbackQuery,
                           )
from aiogram import (Router,
                     Dispatcher,
                     )
from keyboards.buttons import (reg,
                               menu,
                               update,
                               actitity,
                               translators,
                               edit_translator,
                               delete_translator,
                               )


__all__ = ['re', 'CallbackQuery', 'Router',
           'Dispatcher', 'data', 'Message',
           'bot', 'MessageEntity']


__buttons__ = [
    reg,
    menu,
    update,
    actitity,
    translators,
    edit_translator,
    delete_translator
]


def register(dp: Dispatcher) -> None:
    for handler in __buttons__:
        handler.register(dp)
