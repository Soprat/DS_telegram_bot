from keyboards.buttons import *
from keyboards import admin_keyboard
from handlers.admin_menu import create_text
activity = FSM.Form.account_activity

rt = Router()


@rt.callback_query(lambda c: re.search("menu", c.data))
async def admin_menu(query: CallbackQuery):
    FSM.Form.admin_state = 4
    text = create_text(query.from_user.first_name)
    await query.message.edit_text(text)
    await query.message.edit_reply_markup(query.inline_message_id,
                                          reply_markup=admin_keyboard.create_keyboard().as_markup())
    await query.answer()


def register(dp: Dispatcher):
    dp.include_router(rt)
