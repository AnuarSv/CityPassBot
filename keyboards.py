from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from requestsToDB import db
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='City Landmarks')],
], resize_keyboard=True, input_field_placeholder='Select menu item:')


# Formatting data to buttons
async def inline_landmarks():
    landmarks = await db()
    keyboard = InlineKeyboardBuilder()
    for landmark in landmarks:
        keyboard.add(InlineKeyboardButton(text=landmark, callback_data=f'{landmark}'))
    return keyboard.adjust(1).as_markup()
