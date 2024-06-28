from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer


def get_bot(bot_token: str, bot_api: str = None):
    # session = AiohttpSession(api=TelegramAPIServer.from_base(bot_api))
    return Bot(bot_token, parse_mode='HTML')
