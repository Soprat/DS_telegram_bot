import database
from keyboards.buttons import *
import keyboards.translator_keyboard
from handlers.translator_menu import create_text

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("update", c.data))
async def account_activity(query: CallbackQuery):
    await query.answer()
    await query.message.edit_text(text=create_text(translator=query.from_user.id))
    await query.message.edit_reply_markup(reply_markup=keyboards.translator_keyboard.create_keyboard().as_markup())


def register(dp: Dispatcher):
    dp.include_router(rt)
