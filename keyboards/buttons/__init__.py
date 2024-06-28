import logging
import re
from aiogram.types import (CallbackQuery,
                           Message,
                           MessageEntity,
                           )
from aiogram import (Router,
                     Dispatcher,
                     )
from main import bot
import FSM
from keyboards.buttons import (update,
                               actitity,
                               translators,
                               menu,
                               reg,
                               edit_translator,
                               )

__all__ = ['re', 'CallbackQuery', 'Router',
           'Dispatcher', 'FSM', 'Message',
           'bot', 'MessageEntity']


__buttons__ = [
    update,
    actitity,
    translators,
    menu,
    reg,
    edit_translator,
]


def register(dp: Dispatcher) -> None:
    for handler in __buttons__:
        handler.register(dp)
        logging.log(logging.INFO, f'Connected {handler}')
