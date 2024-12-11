import json

with open('dump.json', 'r', encoding='utf-8') as f:     #чтение файла
    data = json.load(f)
special_code = input("Введите код специальности")   #запрос кода специальности у пользователя
found=False
for item in data:
    if item['model'] == 'data.skill' and item['fields']['code'].startswith(special_code):
        print("\n =========================== Найдено ===========================")
        print(f"{item['fields']['code']} >> {item['fields']['title']}")
        found = True
if not found:
    print("\n =========================== Не найдено ===========================")
