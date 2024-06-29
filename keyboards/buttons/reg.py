import database
import pyro
from filters import *
from keyboards.buttons import *

rt = Router(name=__name__)


@rt.callback_query(lambda c: re.search('register_translator', c.data))
async def register_translator(query: CallbackQuery, state: data.FSMContext):
    await state.set_state(data.Form.new_translator_registering)
    await query.answer()
    await bot.send_message(chat_id=query.message.chat.id,
                           text='Пожалуйста, упомяните переводчика через @...')


@rt.message(data.Form.new_translator_registering, F.entities)
async def wait_answer(message: Message):
    for entity in message.entities:
        if entity.type == 'mention':
            user = await pyro.get_id(message, entity)
            answer = database.register_translator(user, message.from_user.id)
            if answer is True:
                await message.answer(f"Удачно добавлен переводчик {entity.extract_from(message.text)}")
            elif answer is False:
                await message.answer("Такой переводчик уже зарегистрирован")
            else:
                print(answer)
                await message.answer("Ошибка!")


def register(dp: Dispatcher):
    dp.include_router(rt)
