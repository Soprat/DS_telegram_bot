import database
from pyro import client
from keyboards.buttons import *
from keyboards import admin_keyboard as keyboard

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("delete_translator", c.data))
async def delete_translator(query: CallbackQuery, state: data.FSMContext):
    await query.answer()
    await state.set_state(data.Form.delete)
    await bot.send_message(query.from_user.id, 'Введите id/username переводчика:')


@rt.message(data.Form.delete)
async def delete(message: Message, state: data.FSMContext):
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
