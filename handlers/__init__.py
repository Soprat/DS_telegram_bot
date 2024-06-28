import FSM
import logging
import re
from aiogram import (Dispatcher,
                     Router,
                     )
from aiogram.types import (Message,
                           MessageEntity,
                           )
from handlers import (get_chat_id,
                      translator_menu,
                      admin_menu,
                      on_startup,
                      )

__all__ = ['FSM', 'logging', 're', 'Dispatcher',
           'Router', 'Message', 'MessageEntity']


__handlers__ = [
    get_chat_id,
    translator_menu,
    admin_menu,
    on_startup,
]


def register(dp: Dispatcher) -> None:
    for handler in __handlers__:
        handler.register(dp)
        logging.log(logging.INFO, f'Connected {handler}')
