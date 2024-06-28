from keyboards import admin_keyboard as keyboard
from keyboards.buttons import *

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("edit_translator", c.data))
async def edit_translator(query: CallbackQuery):
    FSM.Form.admin_state = 2
    await bot.send_message(query.from_user.id, 'Выберите переводчика:')
    await query.message.edit_reply_markup(reply_markup=keyboard.create_keyboard().as_markup())
    await query.answer()


def register(dp: Dispatcher):
    dp.include_router(rt)
