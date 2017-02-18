from datetime import datetime, timedelta


if __name__ == "__main__":

	date_today = datetime.now()

	days_1 = timedelta(days=1)
	months_1 = timedelta(days=30)
	date_prev = date_today - days_1
	date_month_prev = date_today - months_1

	print("Сегодня: {}\nВчера: {}\nМесяц назад: {}".format(date_today.strftime('%d.%m.%Y'), 
		date_prev.strftime('%d.%m.%Y'), date_month_prev.strftime('%d.%m.%Y')))

	date_string = "01/01/17 12:10:03.234567"
	print("Превращаем строку '{}' в объект datetime '{}'".format(date_string, 
		date_today.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')))