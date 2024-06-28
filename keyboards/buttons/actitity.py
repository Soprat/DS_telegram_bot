from keyboards import translator_keyboard as keyboard
from keyboards.buttons import *

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("enter_[12]", c.data))
async def account_activity(query: CallbackQuery):
    i = int(str(query.data).split('_')[-1]) - 1
    FSM.Form.account_activity[i] = not FSM.Form.account_activity[i]
    await query.message.edit_reply_markup(reply_markup=keyboard.create_keyboard().as_markup())
    await query.answer()


def register(dp: Dispatcher):
    dp.include_router(rt)
