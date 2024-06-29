from keyboards.buttons import *
from keyboards import admin_keyboard as keyboard

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("edit_translator", c.data))
async def edit_translator(query: CallbackQuery, state: data.FSMContext):
    await query.answer()
    await state.set_state(data.Form.edit)
    await bot.send_message(query.from_user.id, 'Выберите переводчика:')


@rt.message(data.Form.edit)
async def edit(message: Message, state: data.FSMContext):
    pass


def register(dp: Dispatcher):
    dp.include_router(rt)
