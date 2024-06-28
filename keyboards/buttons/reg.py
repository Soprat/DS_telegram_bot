import database
from keyboards.buttons import *
from filters import *
from pyro import client

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search('register_translator', c.data))
async def register_translator(query: CallbackQuery, state: FSM.FSMContext):
    await state.set_state(FSM.Form.new_translator_registering)
    await bot.send_message(chat_id=query.message.chat.id,
                           text='Пожалуйста, упомяните переводчика через @...')


@rt.message(FSM.Form.new_translator_registering, F.entities, mention_filter)
async def wait_answer(message: Message, mention: MessageEntity):
    for entity in message.entities:
        if entity.type == 'mention_filter':
            username = entity.extract_from(message.text)
            user = await client.get_users(username)
            answer = database.register_translator(user.id, message.from_user.id)
            if answer is True:
                await message.answer(f"Удачно добавлен переводчик {username}")
            else:
                print(answer)
                await message.answer("Ошибка!")


def register(dp: Dispatcher):
    dp.include_router(rt)
