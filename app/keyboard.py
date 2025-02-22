from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Home')],
                                     [KeyboardButton(text='About')]],
                            resize_keyboard=True,
                            input_field_placeholder='Choose a section')

catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='T-shirt', callback_data='t-shirt')],
                                                [InlineKeyboardButton(text='Caps', callback_data='caps')],
                                                [InlineKeyboardButton(text='Sneakers', callback_data='sneakers')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Send phone number', request_contact=True)],
                                          [KeyboardButton(text='Cancel', request_contact=False)]],
                                 resize_keyboard=True)