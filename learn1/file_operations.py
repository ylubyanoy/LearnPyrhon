


if __name__ == "__main__":
	# with open('text.txt', 'w', encoding='utf-8') as f:
	# 	f.write("Привет, мир!\n")

	# with open('text.txt', 'a', encoding='utf-8') as f:
	# 	f.write("Hi!")

	with open('text.txt', 'r', encoding='utf-8') as f:
		for line in f:
			line = line.upper()
			line = line.replace("\n", "")
			print(line)