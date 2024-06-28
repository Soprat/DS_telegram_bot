from aiogram.utils.keyboard import InlineKeyboardBuilder
import FSM

activity = FSM.Form.account_activity


def create_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    builder.button(text=('Вышел' if activity[0] else 'Зашел'), callback_data='enter_1')
    builder.button(text=('Вышел' if activity[1] else 'Зашел'), callback_data='enter_2')
    builder.button(text='Обновить', callback_data='update')
    builder.adjust(2, 1)

    return builder
