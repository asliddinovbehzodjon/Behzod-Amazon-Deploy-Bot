from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    a = KeyboardButton("Telefon raqamizni ulashing",request_contact=True)
    btn.add(a)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!",reply_markup=btn)
@dp.message_handler(types.ContentTypes.CONTACT)
async def contact(message:types.Message):
    await message.answer("Kontakt qabul qilindi!")
