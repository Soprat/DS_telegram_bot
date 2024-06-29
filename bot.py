from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


def get_bot(bot_token: str, bot_api: str = None):
    # session = AiohttpSession(api=TelegramAPIServer.from_base(bot_api))
    return Bot(bot_token, default=DefaultBotProperties(parse_mode='HTML'))
