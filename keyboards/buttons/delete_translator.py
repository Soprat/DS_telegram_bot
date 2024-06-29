import pyro
import database
from keyboards.buttons import *

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
            user_id = await pyro.get_id(message, entity)
            database.delete_translator(user_id)

    await state.clear()


def register(dp: Dispatcher):
    dp.include_router(rt)
