from keyboards.buttons import *
import keyboards.translator_keyboard
from handlers.translator_menu import create_text
import database

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("update", c.data))
async def account_activity(query: CallbackQuery):
    translators = database.get_translators(FSM.Form.user_id)
    data = [database.get_translator_data(translators[0]),
            database.get_translator_data(translators[1])]

    await query.message.edit_text(text=create_text(translator=query.from_user.id))
    await query.message.edit_reply_markup(reply_markup=keyboards.translator_keyboard.create_keyboard().as_markup())
    await query.answer()


def register(dp: Dispatcher):
    dp.include_router(rt)
