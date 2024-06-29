import os
import asyncio
import handlers
from pyro import start
from bot import get_bot
from keyboards import buttons
from dotenv import load_dotenv
from aiogram import Dispatcher
from middlewares import LoggingMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv('settings.env')

BOT_API = os.getenv('BOT_API')
BOT_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher(storage=MemoryStorage())
bot = get_bot(BOT_TOKEN)


async def main() -> None:

    handlers.register(dp)
    buttons.register(dp)
    dp.message.middleware(LoggingMiddleware())
    dp.callback_query.middleware(LoggingMiddleware())
    await start(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
