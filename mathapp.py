import telebot
import random

# SILKA: https://t.me/myMathBotForLesson64868_bot


BOT_TOKEN = '6596894056:AAFwScLkMoTPzCwB1yNMZENqsR1KGTzgkL4'

bot = telebot.TeleBot(BOT_TOKEN)

total_points = 0
question_count = 0

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2
    
    question = f"Masalaning yechimi nima:\n {num1} {operator} {num2}?"
    
    return question, answer

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, "Assalomu Aleykum math bot ga xush kelibsiz!!!")
    global total_points
    global question_count
    total_points = 0
    question_count = 0
    ask_question(message)

def ask_question(message):
    global question_count
    if question_count < 5:
        question, answer = generate_question()
        bot.send_message(message.chat.id, question)
        bot.register_next_step_handler(message, check_answer, answer)
        question_count += 1
    else:
        bot.send_message(message.chat.id, f"O'yin tugadi. Jami to'plangan ballar: {total_points}")
        bot.send_message(message.chat.id, f"Qayta o'ynashni xoxlasangiz /start ni bosing!!!")

def check_answer(message, correct_answer):
    global total_points
    user_answer = message.text
    
    try:
        user_answer = int(user_answer)
    except ValueError:
        bot.send_message(message.chat.id, "Iltimos javobni raqamlar bilan kiriting")
        return
    
    if user_answer == correct_answer:
        total_points += 1
        bot.send_message(message.chat.id, "To'gri! 🎉")
    else:
        bot.send_message(message.chat.id, f"Hato. Bu masalaning javobi: {correct_answer}.")
    
    ask_question(message)

bot.polling()