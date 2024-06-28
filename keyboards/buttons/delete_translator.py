import database
from keyboards import admin_keyboard as keyboard
from keyboards.buttons import *
from pyro import client

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("delete_translator", c.data))
async def delete_translator(query: CallbackQuery, state: FSM.FSMContext):
    FSM.Form.admin_state = 3
    await bot.send_message(query.from_user.id, 'Введите id/username переводчика:')
    await state.set_state(FSM.Form.delete)
    await query.message.edit_reply_markup(reply_markup=keyboard.create_keyboard().as_markup())
    await query.answer()


@rt.message(FSM.Form.delete)
async def delete(message: Message, state: FSM.FSMContext):
    if message.text.isdigit():
        for user_id in message.split(' '):
            database.delete_translator(int(user_id))
    else:
        for entity in message.entities:
            username = entity.extract_from(message.text)
            user = await client.get_users(username)
            database.delete_translator(user.id)

    await state.clear()


def register(dp: Dispatcher):
    dp.include_router(rt)
