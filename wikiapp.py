import telebot
import wikipedia

BOT_TOKEN = '6719577695:AAGtoIx7smO8T-fDsPHDgQ3AxDeNL1lzOSc'

# SILKA: https://t.me/My_WikipediaBot5646_bot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Wiki App ga xush kelibsiz!!!\nNima haqida malumot olmoqchisiz?")

@bot.message_handler(func=lambda message: True)
def search_wikipedia(message):
    wikipedia.set_lang("uz")
    search_query = message.text
    try:
        search_results = wikipedia.search(search_query)
        if search_results:
            page = wikipedia.page(search_results[0])
            summary = page.summary
            images = page.images

            response = f"<b>{page.title}</b>\n\n{summary}"
            bot.reply_to(message, response, parse_mode='HTML')

            if images:
                bot.send_message(message.chat.id, "Bu yerda bu mavzuga doir bazi rasmlar bor:")
                for image in images[:3]:
                    try:
                        bot.send_photo(message.chat.id, image)
                    except Exception as e:
                        print(f"Rasm chiqazishda xatolik yuzaga keldi: {e}")
        else:
            bot.reply_to(message, "Hech narsa topilmadi!")
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        bot.reply_to(message, f"Bu bo'yicha bir nechta natijalar topildi. Iltimos tanlang: {', '.join(options)}")
    except wikipedia.exceptions.PageError:
        bot.reply_to(message, "Hech narsa topilmadi!")
    except Exception as e:
        print(f"Hatolik chiqdi: {e}")

bot.polling()