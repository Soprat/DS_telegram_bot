import data
from handlers import *
from filters import Command
from database import get_translator_data
import keyboards.translator_keyboard as keyboard

rt = Router(name=__name__)


def create_text(translator: str | int = None, account_name: str = None) -> str:
    data_ = get_translator_data(translator)
    print(data_)
    text = f'''Переводчик: {account_name}\n\n'''
    for info in data_:
        text += f'''Имя анкеты: {info['girl_name']}
Баланс за день: {info['day_balance']}
Баланс за месяц: {info['month_balance']}\n\n'''

    return text


@rt.message(Command('menu'), data.Form.translator)
async def send_message(message: Message):
    await message.answer(text=create_text(translator=data.info.user_id,
                                          account_name=message.from_user.first_name),
                         reply_markup=keyboard.create_keyboard().as_markup())


def register(dp: Dispatcher):
    dp.include_router(rt)
