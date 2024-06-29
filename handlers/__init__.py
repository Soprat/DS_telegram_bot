import re
import data
import logging
from aiogram import (Router,
                     Dispatcher,
                     )
from aiogram.types import (Message,
                           MessageEntity,
                           )
from handlers import (admin_menu,
                      on_startup,
                      get_chat_id,
                      translator_menu,
                      )


__all__ = ['data', 'logging', 're', 'Dispatcher',
           'Router', 'Message', 'MessageEntity']


__handlers__ = [
    get_chat_id,
    admin_menu,
    on_startup,
    translator_menu,
    ]


def register(dp: Dispatcher) -> None:
    for handler in __handlers__:
        handler.register(dp)
        logging.log(logging.INFO, f'Connected {handler}')
