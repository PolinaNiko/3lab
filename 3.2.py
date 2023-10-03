file_path = 'детские_товары.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
    exit()

valid_products = []
total_cost = 0
count = 0

for line in lines:
    try:
        name, cost = line.strip().split()
        cost = float(cost)
        if 10 <= cost <= 50:
            valid_products.append((name, cost))
        total_cost += cost
        count += 1
    except ValueError:
        print(f"Ошибка в строке файла: {line}")

print("Товары со стоимостью от 10 до 50 рублей:")
for name, cost in valid_products:
    print(f"{name}: {cost} рублей")

if count > 0:
    average_cost = total_cost / count
    print(f"\nСредняя стоимость всех товаров: {average_cost:.2f} рублей")
else:
    print("\nВ файле нет корректных данных для вычисления средней стоимости.")