import json

file_path = 'firms.txt'

firms_data = []
total_profit = 0
count_profitable = 0

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            name = parts[0]
            revenue = float(parts[2])
            costs = float(parts[3])
            profit = revenue - costs

            if profit >= 0:
                total_profit += profit
                count_profitable += 1

            firms_data.append({name: profit})

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
    exit()

average_profit = total_profit / count_profitable if count_profitable > 0 else 0

result_list = [firms_data, {"average_profit": average_profit}]

with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result_list, result_file)

print("Результат сохранен в файл 'result.json'")
