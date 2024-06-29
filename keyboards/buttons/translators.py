from keyboards.buttons import *
import keyboards.admin_keyboard
from database import get_translators, get_translator_data


rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("translators", c.data))
async def account_activity(query: CallbackQuery):
    data.Form.admin_state = 0
    text = ''
    for translator in get_translators(data.Form.user_id):
        for data_ in get_translator_data(translator):
            text += f"Переводчик {data_['name']}: {data_['girl_name']} | {data_['day_balance']} | {data_['month_balance']}\n"
    await query.message.edit_text(text)
    await query.message.edit_reply_markup(query.inline_message_id,
                                          reply_markup=keyboards.admin_keyboard.create_keyboard().as_markup())
    await query.answer()


def register(dp: Dispatcher):
    dp.include_router(rt)
