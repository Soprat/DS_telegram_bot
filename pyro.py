import os
from pyrogram import Client
from dotenv import load_dotenv
from aiogram.types import MessageEntity, Message
from aiogram.dispatcher.dispatcher import Dispatcher

load_dotenv('settings.env')

client = Client(
            name=__name__,
            bot_token=os.getenv('BOT_TOKEN'),
            api_hash='2e6a788368dff3dd7a9092db18ab053d',
            api_id=25785474,
            no_updates=True)


async def startup() -> None:
    await client.start()


async def shutdown() -> None:
    await client.stop()


async def get_id(message: Message, entity: MessageEntity) -> int:
    username = entity.extract_from(message.text)
    user = await client.get_users(username)
    return user.id


async def start(dp: Dispatcher) -> None:
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
