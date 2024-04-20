from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, callback_data
import parser_usd
import requests
from bs4 import BeautifulSoup
import time



bot = Bot(token='7110748090:AAHbY-WX9M4mdgeZpBZSgsA-zUj7P12CxAk')
dp = Dispatcher()


@dp.message(CommandStart()) # /start
async def start_cmd(message: Message):
    await message.answer('Привет!, это Telegram-bot, который поможет тебе осуществить конвертацию любой из существующих валют!', 
                        reply_markup=get_kb_on_start()
                        )


class ButtonsText:
    COURSES = 'Текущие курсы основных валют'
    CONVERT = 'Конвертировать валюту'
    HELP = 'Помощь'


def get_kb_on_start():                                                # функция, создающая клавиатуру при вызове любой из команд (в await message.x использовать в конце reply_markup=get_kb_on_start())
    button_courses = KeyboardButton(text=ButtonsText.COURSES)
    button_convert = KeyboardButton(text=ButtonsText.CONVERT)
    button_help = KeyboardButton(text=ButtonsText.HELP)
    buttons_first_row = [button_courses]
    buttons_second_row = [button_convert]
    buttons_third_row = [button_help]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_first_row, buttons_second_row, buttons_third_row],
                                 resize_keyboard=True,
                                 input_field_placeholder='Выберите в меню пункт, который Вам требуется.'
                                 )
    return markup


convert_catalog = InlineKeyboardMarkup(inline_keyboard=[              # инлайн кнопки к кнопке конвертации валют
    [InlineKeyboardButton(text='RUB/USD', callback_data='rub/usd')],
    [InlineKeyboardButton(text='RUB/EUR', callback_data='rub/eur')],
    [InlineKeyboardButton(text='RUB/CNY', callback_data='rub/cny')],
    ])


courses_catalog = InlineKeyboardMarkup(inline_keyboard=[              # инлайн кнопки к кнопке курсов валют
    [InlineKeyboardButton(text='USD', callback_data='usd')],
    [InlineKeyboardButton(text='EUR', callback_data='eur')],
    [InlineKeyboardButton(text='CNY', callback_data='cny')],
    ])


@dp.message(CommandStart()) # /start
async def start_cmd(message: Message):
    await message.answer('Привет!, это Telegram-bot, который поможет тебе осуществить конвертацию любой из существующих валют!', 
                        reply_markup=get_kb_on_start()
                        )
  

@dp.message(F.text == ButtonsText.HELP)
async def help(message: Message):
    await message.answer('Вам требуется помощь? Напишите ниже сообщение, раскрыв подробно суть проблемы. Администрация в ближайшее время свяжется с Вами и проблема будет решена.',
                        reply_markup=get_kb_on_start()
                        )


@dp.message(F.text == ButtonsText.CONVERT)
async def convert(message: Message):
    await message.answer('Выберите валютную пару, которая Вам требуется.', reply_markup=convert_catalog)


@dp.message(F.text == ButtonsText.COURSES)
async def courses(message: Message):
    await message.answer('Выберите валюту, курс которой Вас интересует.', reply_markup=courses_catalog)


@dp.callback_query(F.data == 'usd') # курс USD
async def usd_def(callback: CallbackQuery):
    await callback.message.answer(f'Курс USD: {}')

   
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Сейчас бот выключен. Зайдите позже...')