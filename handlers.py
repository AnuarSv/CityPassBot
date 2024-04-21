from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from ChatGPT import gpt
import keyboards as kb
from texts import text_welcome
from requestsToDB import db_choose
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Hello, {text_welcome}', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('City Pass Astana Bot это бот который позволяет удобно пользоваться CityPass')


@router.message(F.text == 'City Landmarks')
async def show_db_names(message: Message):
    await message.answer('All Astana\'s landmarks', reply_markup=await kb.inline_landmarks())


@router.callback_query()
async def info(callback: CallbackQuery):
    landmark_name = callback.data
    await callback.answer(f'Info: {landmark_name}')
    await callback.message.answer(f'Info about: \n{await db_choose(landmark_name)}')


@router.message(F.text)
async def cmd_answer(message: Message):
    response = await gpt(message.text)
    await message.answer(response)




# -----------------------------------------------------------------------------------------------

# @router.message(Command('get_photo'))
# async def get_photo(message: Message):
#     await message.answer_photo(photo='url-photo', caption='Маршрут построен.')
