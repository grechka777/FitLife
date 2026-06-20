# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
LITERS_PER_KG = 1000

print('Здравствуйте! Вас приветствует программ: "Fit Life".')


# # проверить введено ли число
# def get_number_input(prompt: str):
#     while True:
#         user_input = input(prompt)
#         try:
#             number = float(user_input)
#             return number
#         except ValueError:
#             ...

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь
# преобразовать в число)
user_name = input("Введите, пожалуйста, ваше имя: ")
user_age = input("Введите, пожалуйста, ваш возраст: ")
user_age = int(user_age)

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height
# (тип float)
user_weight = input("Введите, ваш вес (кг. например: '75.5'): ")
user_weight = float(user_weight)
user_height = input("Введите, ваш рост (в метрах, например: '1.75'): ")
user_height = float(user_height)

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = user_weight * WATER_PER_KG

# Переводим в литры
water_needed = round((water_ml / LITERS_PER_KG), 2)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"\nПривет, {user_name}")
print(f"Отчет для пользователя: {user_name}")
print(f"Ваш возраст: {user_age}")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed} л. в день")


print("Расчет окончен. Будьте здоровы!")
