import telebot
from setuptools.command.build import build
from telebot import types

def main_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Ввести запрос")
    button2 = types.KeyboardButton(text="О создателе бота")
    button3 = types.KeyboardButton(text="Помощь")
    button4 = types.KeyboardButton(text="Изменить версию GPT")
    kb.add(button, button2, button3, button4)
    return kb
def change_version_in():
    kb = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton(text="GPT-3.5-turbo", callback_data="GPT-3.5-turbo")
    button2 = types.InlineKeyboardButton(text="GPT-4-turbo", callback_data="GPT-4-turbo")
    button3 = types.InlineKeyboardButton(text="GPT-4o", callback_data="GPT-4o")
    button4 = types.InlineKeyboardButton(text="GPT-4", callback_data="GPT-4")
    button5 = types.InlineKeyboardButton(text="GPT-3", callback_data="GPT-3")
    button6 = types.InlineKeyboardButton(text="GPT-4o-mini", callback_data="GPT-4o-mini")
    kb.row(button2, button)
    kb.row(button3, button6)
    kb.row(button4, button5)
    return kb
def is_subs():
    kb = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton(text="Подписаться", url= "https://t.me/workm5")
    button2 = types.InlineKeyboardButton(text="Готово", callback_data="right")
    kb.row(button, button2)
    return kb