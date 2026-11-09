import telebot
from telebot import types

# Твой токен
BOT_TOKEN = '9206146032:AAFCPf9EL0ihmgPuEc2HvVFHYmVRMTyV67g'
bot = telebot.TeleBot(BOT_TOKEN)

# --- ТЕКСТЫ ДЛЯ ДЕМКИ ---
NAME_COMPANY = "Prime Solutions"
TEXT_START = f"Добро пожаловать в {NAME_COMPANY}! 👋\nВыберите нужный раздел в меню ниже:"
TEXT_CONTACT = "📞 Связаться с нами:\nТелефон: +7 (999) 123-45-67\nTelegram: @krozzet_dev\n\nМы на связи с 10:00 до 20:00."
TEXT_REVIEWS = "⭐ Что о нас говорят клиенты:\n\n1. «Очень быстро и качественно, рекомендую!»\n2. «Приятные цены, вежливый персонал.»\n3. «Заказываю уже третий раз, все супер.»"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🛒 Каталог")
    btn2 = types.KeyboardButton("⭐ Отзывы")
    btn3 = types.KeyboardButton("📞 Связаться")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, TEXT_START, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🛒 Каталог":
        inline_markup = types.InlineKeyboardMarkup(row_width=1)
        
        btn_item1 = types.InlineKeyboardButton("Услуга 1 — 1000 ₽", callback_data="item1")
        btn_item2 = types.InlineKeyboardButton("Услуга 2 — 2000 ₽", callback_data="item2")
        btn_item3 = types.InlineKeyboardButton("Услуга 3 — 3000 ₽", callback_data="item3")
        inline_markup.add(btn_item1, btn_item2, btn_item3)
        
        bot.send_message(message.chat.id, "📋 Наш каталог. Нажмите на позицию, чтобы узнать подробности:", reply_markup=inline_markup)

    elif message.text == "⭐ Отзывы":
        bot.send_message(message.chat.id, TEXT_REVIEWS)
        
    elif message.text == "📞 Связаться":
        bot.send_message(message.chat.id, TEXT_CONTACT)
        
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите пункт из меню ниже 👇")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "item1":
        bot.send_message(call.message.chat.id, f"Вы выбрали: Услуга 1.\nЦена: 1000 ₽.\n\nЧтобы заказать, напишите нашему менеджеру: @krozzet_dev")
    elif call.data == "item2":
        bot.send_message(call.message.chat.id, f"Вы выбрали: Услуга 2.\nЦена: 2000 ₽.\n\nЧтобы заказать, напишите нашему менеджеру: @krozzet_dev")
    elif call.data == "item3":
        bot.send_message(call.message.chat.id, f"Вы выбрали: Услуга 3.\nЦена: 3000 ₽.\n\nЧтобы заказать, напишите нашему менеджеру: @krozzet_dev")
    
    bot.answer_callback_query(call.id)

print("Демо-бот запущен!")
bot.polling(none_stop=True)
