from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from time import sleep
from app import keyboard as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    city = State()
    phone_number = State()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Hello!', reply_markup=kb.main)
    await message.reply('I am a bot that can fart. Just type /fart')
    commands = [
        "/start - Start the bot",
        "/fart - Make the bot fart",
        "/Register - Register a new user",
        "hi - Greet the bot",
        "fire - Send a fire emoji",
        "fuck you - Swear at the bot",
        "Catalog - Get the catalog of goods"
    ]
    await message.answer("\n".join(commands))

@router.message(Command('fart'))
async def cmd_fart(message: types.Message):
    await message.answer('😶‍🌫️')

@router.message(F.text == 'hi')
async def hi(message: types.Message):
    await message.answer('Hello!')

@router.message(F.text == 'fire')
async def fire(message: types.Message):
    await message.answer('🔥')

@router.message(F.text == 'fuck you')
async def swear(message: types.Message):
    await message.answer('.....')
    sleep(2)
    await message.answer('🖕')

@router.message(F.text == 'Catalog' or F.text == 'catalog')
async def get_catalog(message: types.Message):
    await message.answer('Choose the category of goods', reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirts(callback: types.CallbackQuery):
    await callback.answer("You've chosen a category", show_alert=True)
    await callback.message.answer('So you want to but a T-shirt?')
    sleep(1)
    await callback.message.answer("That's awesome!!!")

@router.message(Command('Register'))
async def cmd_register(message: types.Message, state: FSMContext):
    await message.answer("Let's get you registered. What's your name?")
    await state.set_state(Register.name)

@router.message(Register.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("How old are you?")
    await state.set_state(Register.age)

@router.message(Register.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Which city do you live in?")
    await state.set_state(Register.city)

@router.message(Register.city)
async def process_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Register.phone_number)
    await message.answer("What's your phone number?", reply_markup=kb.get_number)

@router.message(Register.phone_number, F.contact)
async def process_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    user_data = await state.get_data()
    await message.answer(f"Registration complete!\nName: {user_data['name']}\nAge: {user_data['age']}\nCity: {user_data['city']}\nPhone Number: {user_data['phone_number']}")
    await state.clear()

@router.message(F.text == 'Cancel')
async def cancel_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Registration canceled.", reply_markup=kb.main)


