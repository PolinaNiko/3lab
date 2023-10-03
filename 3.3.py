file_path = 'учебные_предметы.txt'
subjects_dict = {}
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(':')
            subject = parts[0].strip()
            lessons_info = parts[1].split()

            total_lessons = 0
            for lesson in lessons_info:
                count, _ = lesson.split('(')
                total_lessons += int(count)

            subjects_dict[subject] = total_lessons

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
    exit()

print("Словарь с общим количеством занятий по каждому предмету:")
print(subjects_dict)
