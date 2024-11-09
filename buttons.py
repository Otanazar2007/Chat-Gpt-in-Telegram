import telebot
from setuptools.command.build import build
from telebot import types

def main_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Ввести запрос")
    button5 = types.KeyboardButton(text="Генерация изображения")
    button2 = types.KeyboardButton(text="О создателе бота")
    button3 = types.KeyboardButton(text="Помощь")
    button4 = types.KeyboardButton(text="Изменить версию GPT")
    kb.add(button, button5, button2, button3, button4)
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
def feedback():
    kb = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text="Неверный ответ?", callback_data="error")
    kb.row(button)
    return kb
def image_in():
    kb = types.InlineKeyboardMarkup(row_width=3)
    button1 = types.InlineKeyboardButton(text="FLUX", callback_data="flux")
    button2 = types.InlineKeyboardButton(text="FLUX PRO", callback_data="flux-pro")
    button3 = types.InlineKeyboardButton(text="FLUX REALISM", callback_data="flux-realism")
    button4 = types.InlineKeyboardButton(text="FLUX ANIME", callback_data="flux-anime")
    button5 = types.InlineKeyboardButton(text="FLUX 3D", callback_data="flux-3d")
    button6 = types.InlineKeyboardButton(text="FLUX DISNEY", callback_data="flux-disney")
    button7 = types.InlineKeyboardButton(text="FLUX PIXEL", callback_data="flux-pixel")
    button8 = types.InlineKeyboardButton(text="FLUX 4o", callback_data="flux-4o")
    button9 = types.InlineKeyboardButton(text="FLUX SCHNELL", callback_data="flux-schnell")
    kb.row(button1, button2, button3)
    kb.row(button4, button5, button6)
    kb.row(button7, button8, button9)
    return kb