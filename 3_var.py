# Типы данных

# целочисленный тип данных (int, integer)

my_int = 124125

# числа с плавающей точкой (вещественные числа) (float)
my_float = 352.345

# булевы значения (bool, boolean)
# в честь Джорджа Буля (Булева алгебра)

# логическая 1
bool_1 = True

# логическая 0
bool_0 = False

# строковые значения (символы, слова, тексты) (str, string)
my_char = 'A'
my_string = 'python'
my_text = 'Моя мотивация'

multi_text = '''много
строчный
текст'''

my_text = 'Где твоя "мотивация"'

# способы форматирования строк
str_1 = "Температура котла = "
temp = 75.73464576
str_2 = "*C"

# 1. Конкатенация (объединение) строк - старый способ

result = str_1 + str(temp) + str_2

# 2. f-string (f-строка) - новый способ

result = f"Температур котла = {temp:.2f} {str_2}"
# print(result)

# арифметические операции

a = 10
b = 5

# сложение
result = a + b

# вычитание
result = a - b

# умножение
result = a * b

# вычитание
# всегда возвращает число с плавающей точкой
result = a / b

# целочичленное деление
# всегда возвращает целую часть результата
result = a // b

# деление по остатку
result = a % b

# возведение в степень
a = 9
b = 2
result = a ** (1/b)

import math

result = math.sqrt(100)

print(result)


