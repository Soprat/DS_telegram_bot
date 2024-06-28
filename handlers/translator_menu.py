from handlers import *
from filters import Command
import keyboards.translator_keyboard as keyboard
from database import get_translator_data

rt = Router(name=__name__)


def create_text(translator: str | int = None, account_name: str = None) -> str:
    data = get_translator_data(translator)

    text = f'''
Переводчик: {account_name}

Имя анкеты: {data[0]['girl_name']}
Баланс за день: {data[0]['day_balance']}
Баланс за месяц: {data[0]['month_balance']}

Имя анкеты: {data[1]['girl_name']}
Баланс за день: {data[1]['day_balance']}
Баланс за месяц: {data[1]['month_balance']}
'''

    return text


@rt.message(Command('menu'), FSM.Form.translator)
async def send_message(message: Message):
    await message.answer(text=create_text(translator=message.from_user.id,
                                          account_name=message.from_user.first_name),
                         reply_markup=keyboard.create_keyboard().as_markup())


def register(dp: Dispatcher):
    dp.include_router(rt)
