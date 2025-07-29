import telebot
from datetime import datetime

TOKEN = "8364296250:AAHqaby4QrAF9vhLKyoMZIf50g1RlrZ-2MM"
ADMIN_ID = 7472223632# <- bu yerga o‘zingizning ID’ingizni yozing

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "👋 Salom! Menga matn yuboring — men uni takrorlayman.\n"
                          "📌 /reverse — matnni teskari qiladi\n"
                          "📌 /time — hozirgi vaqt\n"
                          "📌 /id — Telegram ID\n"
                          "📌 /upper — matnni katta harfga o‘zgartiradi")

@bot.message_handler(commands=['reverse'])
def reverse_text(message):
    text = message.text.replace('/reverse', '').strip()
    if text:
        bot.reply_to(message, text[::-1])
    else:
        bot.reply_to(message, "❗ Iltimos, matn yuboring: /reverse Salom")

@bot.message_handler(commands=['time'])
def current_time(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, f"⏰ Hozirgi vaqt: {now}")

@bot.message_handler(commands=['id'])
def get_user_id(message):
    bot.reply_to(message, f"🆔 Sizning Telegram ID’ingiz: {message.from_user.id}")

@bot.message_handler(commands=['upper'])
def upper_text(message):
    text = message.text.replace('/upper', '').strip()
    if text:
        bot.reply_to(message, text.upper())
    else:
        bot.reply_to(message, "❗ Iltimos, matn yuboring: /upper matn")

# 🖼 Rasm kelganda admin'ga yuboradi
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=f"📸 {message.from_user.first_name} dan rasm keldi!")

# 🎵 Audio kelganda admin'ga yuboradi
@bot.message_handler(content_types=['audio', 'voice'])
def handle_audio(message):
    file_id = message.voice.file_id if message.voice else message.audio.file_id
    bot.send_message(ADMIN_ID, f"🎵 {message.from_user.first_name} dan audio keldi.")
    bot.send_voice(ADMIN_ID, file_id)

# ✉️ Boshqa xabarlarga oddiy echo
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
