from handlers import *
from aiogram.filters import Command
import keyboards.admin_keyboard as keyboard

rt = Router(name=__name__)
logging.log(logging.INFO, f'Started router {__name__}')


def create_text(user_name) -> str:
    text = f'''
Привет, {user_name}
Задания на сегодня: 
1) Проверка анкеты
2) Скинуть баланс за вчерашний день
'''

    return text


@rt.message(Command('menu'), FSM.Form.admin)
async def send_message(message: Message):
    first_name = message.from_user.first_name if message.from_user.first_name else ''
    last_name = message.from_user.last_name if message.from_user.last_name else ''
    await message.answer(text=create_text(first_name + last_name),
                         reply_markup=keyboard.create_keyboard().as_markup())


def register(dp: Dispatcher):
    dp.include_router(rt)
