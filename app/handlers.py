from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from time import sleep
from app import keyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Hello!', reply_markup=kb.main)
    await message.reply('I am a bot that can help you with shopping. Choose a category of goods')

@router.message(F.text == 'hi')
async def hi(message: types.Message):
    await message.answer('Hello!')

@router.message(F.text == 'fire')
async def fire(message: types.Message):
    await message.answer('🔥')

@router.message(F.text == 'Catalog' or F.text == 'catalog')
async def get_catalog(message: types.Message):
    await message.answer('Choose the category of goods', reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirts(callback: types.CallbackQuery):
    await callback.answer("You've chosen a category", show_alert=True)
    await callback.message.answer('So you want to but a T-shirt?')
    sleep(1)
    await callback.message.answer("That's awesome!!!")