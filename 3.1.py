import string

with open('F1.txt', 'w') as f1:
    print("Введите данные для записи в файл F1. Пустая строка завершит ввод.")
    while True:
        line = input()
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1:
    first_line = f1.readline()
    words = first_line.split()
    second_word = words[1].strip(string.punctuation) if len(words) >= 2 else ""

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        words = line.split()
        if second_word and any(word.strip(string.punctuation) == second_word for word in words):
            f2.write(line)

with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    if lines:
        last_line = lines[-1].rstrip()
        digit_count = sum(c.isdigit() for c in last_line)
        print(f"Количество цифр в последней строке файла F2: {digit_count}")
    else:
        print("Файл F2 пуст.")