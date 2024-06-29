from keyboards.buttons import *
from keyboards import translator_keyboard as keyboard
import database

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search("enter_[12]", c.data))
async def account_activity(query: CallbackQuery):
    account = int(str(query.data).split('_')[-1]) - 1  # 0 or 1
    translator_data = database.get_translator_data(data.info.user_id)
    await query.bot.send_message(
        chat_id=database.get_admin(data.info.user_id),
        text=f'Переводчик {query.from_user.first_name} вышел с аккаунта {translator_data[account]["girl_name"]}'
        if data.info.account_activity[account] else
        f'Переводчик {query.from_user.first_name} зашел на аккаунт {translator_data[account]["girl_name"]}')
    data.info.account_activity[account] = not data.info.account_activity[account]
    await query.answer()
    await query.message.edit_reply_markup(
        reply_markup=keyboard.create_keyboard().as_markup())


def register(dp: Dispatcher):
    dp.include_router(rt)
