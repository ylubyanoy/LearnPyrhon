from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

API_KEY = "224022706:AAGiInxRBkNj9z23qtUrFbgQ2Z8VXgAwr-0"

def main():
    updater = Updater(API_KEY)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    # dp.add_handler(CommandHandler("calc_word", calc_word_data))
    dp.add_handler(CommandHandler("calc_keyboard", show_keyboard))

    dp.add_error_handler(show_error)

    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()

def wordcount(bot, update):
    print('Вызван /wordcount')
    print(update.message)

    user_str = update.message['text'].split("\"")[1]
    if len(user_str) >= 3:
        user_count = user_str.split(" ")
    else:
        bot.sendMessage(update.message.chat_id, text="Введите предложение для подсчета слов")

    bot.sendMessage(update.message.chat_id, text="Количество слов в предложении {} - {}".format(user_str, len(user_count)))

def show_keyboard(bot, update):

    custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=update.message.chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)

def greet_user(bot, update):
    print('Вызван /start')
    print(update.message)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    
    # result = calc_user_data(update.message.text)
    result = calc_word_data(update.message.text)

    bot.sendMessage(update.message.chat_id, result)

def calc_word_data(message_text):
    word_calc = "сколько будет три минус два"
    dict_digits = {'один': 1, 'два': 2, 'три': 3,
                    'четыре': 4, 'пять': 5, 'шесть': 6,
                    'семь': 7, 'восемь':8, 'девять': 9, 'десять': 10}

    print(word_calc)                
    print(word_calc[14:])               
    


    # calc_str = message_text
    # if calc_str[-1] == "=":
    #   calc_str = calc_str[:-1]

    #   result = 0
    #   if "+" in calc_str:
    #       for x in calc_str.split("+"):
    #           try:
    #               result += int(x)
    #           except (TypeError, ValueError):
    #               return "Должно быть два числа"
    #       return result

    #   elif "-" in calc_str:
    #       for x in calc_str.split("-"):
    #           try:
    #               result += int(x)
    #           except (TypeError, ValueError):
    #               return "Должно быть два числа"
    #       return result

    #   elif "*" in calc_str:
    #       for x in calc_str.split("*"):
    #           try:
    #               result += int(x)
    #           except (TypeError, ValueError):
    #               return "Должно быть два числа"

    #       bot.sendMessage(update.message.chat_id, result)
    #   elif "/" in calc_str:
    #       for x in calc_str.split("-"):
    #           try:
    #               result += int(x)
    #           except (TypeError, ValueError, ZeroDivisionError):
    #               return "Должно быть два числа"
    #       return result

def calc_user_data(message_text):
    calc_str = message_text
    if calc_str[-1] == "=":
        calc_str = calc_str[:-1]

        result = 0
        if "+" in calc_str:
            for x in calc_str.split("+"):
                try:
                    result += int(x)
                except (TypeError, ValueError):
                    return "Должно быть два числа"
            return result

        elif "-" in calc_str:
            for x in calc_str.split("-"):
                try:
                    result += int(x)
                except (TypeError, ValueError):
                    return "Должно быть два числа"
            return result

        elif "*" in calc_str:
            for x in calc_str.split("*"):
                try:
                    result += int(x)
                except (TypeError, ValueError):
                    return "Должно быть два числа"

            bot.sendMessage(update.message.chat_id, result)
        elif "/" in calc_str:
            for x in calc_str.split("-"):
                try:
                    result += int(x)
                except (TypeError, ValueError, ZeroDivisionError):
                    return "Должно быть два числа"
            return result

    
if __name__ == "__main__":
    main()  