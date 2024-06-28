from aiogram.utils.keyboard import InlineKeyboardBuilder
from FSM import Form

activity = Form.account_activity


def create_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    state = Form.admin_state
    buttons = [
               {'text': 'Переводчики', 'callback_data': 'translators'},
               {'text': 'Зарегестрировать', 'callback_data': 'register_translator'},
               {'text': 'Редактировать', 'callback_data': 'edit_translator'},
               {'text': 'Удалить', 'callback_data': 'delete_translator'}
               ]
    if state != 4:
        buttons[state] = {'text': 'Меню', 'callback_data': 'menu'}

    for button in buttons:
        builder.button(text=button['text'], callback_data=button['callback_data'])

    builder.adjust(2, 1)

    return builder
