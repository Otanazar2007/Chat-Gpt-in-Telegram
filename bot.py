import time
from tabnanny import check

import telebot
from g4f.models import gpt_35_turbo, gpt_4, gpt_4o_mini
import g4f
from pyexpat.errors import messages
import database
import buttons
from buttons import change_version_in
from g4f.client import Client
import token
user_requests = {}
channel_id = "-1002433291625"
bot = telebot.TeleBot(token = "7908371003:AAEUAOv8R9CC3iAgUDWCgrd3O4FB_beAlX4")
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Привет! Этот бот отправляет твои запросы в ChatGpt! К сожалению разработчик ломает голову почему он не работает")
    try:
        status = bot.get_chat_member(chat_id=channel_id, user_id=user_id).status
        if status in ["member", "administrator", "creator"]:
            bot.send_message(user_id, "Добро пожаловать обратно!" ,reply_markup=buttons.main_menu_kb())
        else:
            bot.send_message(user_id, "Бот бесплатен а запросы не ограничены\nПорадуйте админа подпиской", reply_markup=buttons.is_subs())
    except Exception as e:
        bot.send_message(user_id, "Вы не подписаны!", reply_markup=buttons.is_subs())
@bot.message_handler(func=lambda message: message.text == "Ввести запрос")
def second_step(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Введите свой запрос\nВажно!\nФотографии не обрабатываются")
    bot.register_next_step_handler(message, answer)
def answer(message):
    user_id = message.from_user.id
    ver = database.for_gpt(user_id)
    print(ver)
    if ver == ('GPT-3.5-turbo',):
        processing = bot.send_message(user_id,"Ваш запрос обрабатывается...")
        bot.send_chat_action(user_id, action="typing")
        client = Client
        response = g4f.ChatCompletion.create(
            model=gpt_35_turbo,
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        bot.send_message(user_id, f"{response}\nВерсия Chat Gpt 3.5", reply_markup=buttons.feedback())
        bot.delete_message(user_id, processing.message_id)
    elif ver == ('GPT-4-turbo',):
        processing = bot.send_message(user_id, "Ваш запрос обрабатывается...")
        bot.send_chat_action(user_id, action="typing")
        client = Client
        response = g4f.ChatCompletion.create(
            model=gpt_4,
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        bot.send_message(user_id, f"{response}\nВерсия Chat Gpt 4 turbo", reply_markup=buttons.feedback())
        bot.delete_message(user_id, processing.message_id)
    elif ver == ('GPT-4o',):
        processing = bot.send_message(user_id, "Ваш запрос обрабатывается...")
        bot.send_chat_action(user_id, action="typing")
        client = Client
        response = g4f.ChatCompletion.create(
            model=gpt_4,
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        bot.send_message(user_id, f"{response}\nВерсия Chat Gpt 4o", reply_markup=buttons.feedback())
        bot.delete_message(user_id, processing.message_id)
    elif ver == ('GPT-4',):
        processing = bot.send_message(user_id, "Ваш запрос обрабатывается...")
        bot.send_chat_action(user_id, action="typing")
        client = Client
        response = g4f.ChatCompletion.create(
            model=gpt_4,
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        bot.send_message(user_id, f"{response}\nВерсия Chat Gpt 4", reply_markup=buttons.feedback())
        bot.delete_message(user_id, processing.message_id)
    elif ver == ('GPT-3',):
        processing = bot.send_message(user_id, "Ваш запрос обрабатывается...")
        bot.send_chat_action(user_id, action="typing")
        client = Client
        response = g4f.ChatCompletion.create(
            model=gpt_35_turbo,
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        bot.send_message(user_id, f"{response}\nВерсия Chat Gpt 3", reply_markup=buttons.feedback())
        bot.delete_message(user_id, processing.message_id)
    elif ver == ('GPT-4o-mini',):
        processing = bot.send_message(user_id, "Ваш запрос обрабатывается...")
        bot.send_chat_action(user_id, action="typing")
        client = Client
        response = g4f.ChatCompletion.create(
            model=gpt_4o_mini,
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        bot.send_message(user_id, f"{response}\nВерсия Chat Gpt 4o mini", reply_markup=buttons.feedback())
        bot.delete_message(user_id, processing.message_id)
@bot.message_handler(func=lambda message: message.text == "Генерация изображения")
def ask_image_text(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Введите описание ткста")
    bot.register_next_step_handler(message, ask_image)
def ask_image(message):
    user_id = message.from_user.id
    request = message.text
    user_requests[user_id] = request
    bot.send_message(user_id, "Выберите нейронку для обработки!", reply_markup=buttons.image_in())
@bot.callback_query_handler(lambda call: call.data in ['flux',
'flux-pro',
'flux-realism',
'flux-anime',
'flux-3d',
'flux-disney',
'flux-pixel',
'flux-4o',
'flux-schnell'])
def model_choice(call):
    user_id = call.message.chat.id
    model_ = call.data
    request = user_requests.get(user_id)
    if request:
        bot.send_message(user_id, f"Выбран модель {model_}")
        user_requests.pop(user_id, None)
        print(model_)
        print(request)
        print(user_id)
        try:
            bot.send_chat_action(user_id, "upload_photo")
            client = Client()
            response = client.images.generate(
                model=f"{model_}",
                prompt=f"{request}",
            )
            image_url = response.data[0].url
            bot.send_photo(user_id, image_url, caption=f"Изображение под запрос {request}\n"
                                                       f"Модель{model_}", reply_markup=buttons.feedback())
        except:
            bot.send_message(user_id, "Ошибка при генерации фото")
    else:
        bot.send_message(user_id, "Ошибка")
@bot.message_handler(func=lambda message: message.text == "О создателе бота")
def about_dv(message):
    user_id = message.from_user.id
    bot.send_chat_action(user_id, action="typing")
    bot.send_message(user_id, "ГЕО - Узбекистан, Ташкент +2 от МСК\n"
                              "Возраст - 17\n"
                              "Язык программирования - Python\n"
                              "Контакт - @kadambaev_o")
@bot.message_handler(func=lambda message: message.text == "Помощь")
def help(message):
    user_id = message.from_user.id
    bot.send_chat_action(user_id, action="typing")
    bot.send_message(user_id, "Привет! Я могу помочь с различными вопросами: "
                              "от общих знаний и информации о текущих событиях до "
                              "помощи в учёбе, программировании, планировании поездок и многом другом. "
                              "Можешь спросить меня о чём угодно, и я постараюсь тебе помочь!")
@bot.message_handler(func=lambda message: message.text == "Изменить версию GPT")
def change_ver_kb(message):
    user_id = message.from_user.id
    change_ver = bot.send_message(user_id, "Выберите подходящую версию Chat,a", reply_markup=change_version_in())
@bot.callback_query_handler(lambda call: "GPT-3.5-turbo" in call.data)
def verl(call):
    user_id = call.message.chat.id
    bot.send_chat_action(user_id, action="typing")
    ver = call.data
    database.change_verson(user_id, ver)
    bot.send_message(user_id,"Вы выбрали версию GPT-3.5-turbo!")
@bot.callback_query_handler(lambda call: "GPT-4-turbo" in call.data)
def newest_ver(call):
    user_id = call.message.chat.id
    bot.send_chat_action(user_id, action="typing")
    ver = call.data
    database.change_verson(user_id, ver)
    bot.send_message(user_id, "Вы выбрали версию GPT-4-turbo!")
@bot.callback_query_handler(lambda call: "GPT-4o-mini" in call.data)
def verq(call):
    user_id = call.message.chat.id
    bot.send_chat_action(user_id, action="typing")
    ver = call.data
    database.change_verson(user_id, ver)
    bot.send_message(user_id, "Вы выбрали версию GPT-4o-mini")
@bot.callback_query_handler(lambda call: "GPT-3" in call.data)
def verv(call):
    user_id = call.message.chat.id
    bot.send_chat_action(user_id, action="typing")
    ver = call.data
    database.change_verson(user_id, ver)
    bot.send_message(user_id, "Вы выбрали версию GPT-3")
@bot.callback_query_handler(lambda call: "GPT-4" in call.data)
def vert(call):
    user_id = call.message.chat.id
    bot.send_chat_action(user_id, action="typing")
    ver = call.data
    database.change_verson(user_id, ver)
    bot.send_message(user_id, "Вы выбрали версию GPT-4")
@bot.callback_query_handler(lambda call: "GPT-4o" in call.data)
def vera(call):
    user_id = call.message.chat.id
    bot.send_chat_action(user_id, action="typing")
    ver = call.data
    database.change_verson(user_id, ver)
    bot.send_message(user_id, "Вы выбрали версию GPT-4o")
@bot.callback_query_handler(lambda call: "right" in call.data)
def check_user(call):
    user_id = call.message.chat.id
    try:
        status = bot.get_chat_member(chat_id=channel_id, user_id=user_id).status
        if status in ["member", "administrator", "creator"]:
            bot.send_message(user_id, "Добро пожаловать!", reply_markup=buttons.main_menu_kb())
        else:
            bot.send_message(user_id, "Нет, не обманешь", reply_markup=buttons.is_subs())
    except Exception as e:
        bot.send_message(user_id, "Вы не подписаны!", reply_markup=buttons.is_subs())
@bot.callback_query_handler(lambda call: "error" in call.data)
def feedback(call):
    user_id = call.message.chat.id
    bot.send_message(user_id, "Напишите свой отзыв,а затем отправьте его мне!")
    bot.register_next_step_handler(call.message, feedback_otlov)
def feedback_otlov(message):
    user_id = message.from_user.id
    message = message.text
    print(message)
    bot.send_message(user_id,"Спасибо за ваш отзыв!", reply_markup=buttons.main_menu_kb())
    bot.send_message(-4592099015, f"Ошибка!\nUser_id - {user_id}\nТекст-\n{message}")
@bot.message_handler(commands=["broadcast"])
def brdcast(message):
    user_id = message.from_user.id
    if message.from_user.id == 6967192344:
        bot.send_message(6967192344, "Введите текст для рассылки")
        bot.register_next_step_handler(message, next_step_brodcast)
    else:
        bot.send_message(user_id, "У вас не прав администратора")
def next_step_brodcast(message):
    brodcast_text = message.text
    users = database.all_users()
    print(users)
    for user in users:
        try:
            bot.send_message(user, brodcast_text)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user}: {e}")
    bot.send_message(6967192344, "Рассылка завершена")
bot.infinity_polling()