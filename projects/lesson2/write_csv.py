import csv


if __name__ == "__main__":

	answers = {'привет': "И тебе привет!", 'как дела': "Лучше всех", 'пока': "Увидимся"}

	with open('answers.csv', 'w', encoding='utf-8') as f:
		fields = ['question', 'answer']
		writer = csv.DictWriter(f, fields, delimiter=';')
		writer.writeheader()
		for key, value in answers.items():
			writer.writerow({'question': key, 'answer': value})