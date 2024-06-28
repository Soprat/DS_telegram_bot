from handlers import *
from aiogram.filters import Command

rt = Router(name=__name__)
logging.log(logging.INFO, f'Started router {__name__}')


@rt.message(Command('get_chat_id'))
async def get_id(message: Message):
    await message.answer(str(message.chat.id))


def register(dp: Dispatcher):
    dp.include_router(rt)
