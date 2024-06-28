import asyncio
import logging
import os
import sys
from bot import get_bot
from dotenv import load_dotenv
from aiogram import Dispatcher
from pyro import start
import handlers
from keyboards import buttons
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv('settings.env')

BOT_API = os.getenv('BOT_API')
BOT_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher(storage=MemoryStorage())
bot = get_bot(BOT_TOKEN)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s|%(levelname)s|%(name)s|%(message)s",
        datefmt="%Y-%m-%d|%H:%M:%S",
        stream=sys.stdout)

    handlers.register(dp)
    buttons.register(dp)
    await start(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
