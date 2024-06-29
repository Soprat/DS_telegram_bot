import database
from handlers import *
from pyro import client
from filters import CommandStart

rt = Router(name=__name__)


@rt.message(CommandStart())
async def on_startup(message: Message, state: data.FSMContext):
    data.info.user_id = message.from_user.id
    await state.set_state(data.Form.bot_registering)
    await message.answer(f"Привет, {message.from_user.first_name}. \nПожалуйста, введи ник админа или свой ключ:")


@rt.message(data.Form.bot_registering)
async def bot_registering(message: Message, state: data.FSMContext):
    if 'mention' in [entity.type for entity in message.entities]:
        username = message.entities[-1].extract_from(message.text)
        user = await client.get_users(username)
        if f'{user.id}' in database.get_admins():
            await state.set_state(data.Form.translator)
            await message.reply("Вы успешно вошли!")
    key = re.findall(r'[0-9]*9', message.text)
    if key:
        if database.get_keys():
            await state.set_state(data.Form.admin)
            await message.reply("Добро пожаловать!")


def register(dp: Dispatcher):
    dp.include_router(rt)
