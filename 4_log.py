# операции сравнения

x = 3
y = 4

# операции равенства (равно)
# мы справшиваем "значение х равно значению у"
res = x == y

# операции равенства (не равно)
# мы справшиваем "значение х НЕ равно значению у"
res = x != y

# операции равенства (больше)
# мы справшиваем "значение х больше значению у"
res = x > y

# операции равенства (меньше)
# мы справшиваем "значение х меньше значению у"
res = x < y

# операции равенства (меньше либо равно)
# мы справшиваем "значение х меньше либо равно значению у"
res = x <= y

# операции равенства (больше либо равно)
# мы справшиваем "значение х больше либо равно значению у"
res = x >= y

# логические операции

var_1 = True
var_2 = False

# оператор "НЕ" (НОТ, операция инверция)
res = not var_1

# оператор "И" (AND, операция конъюнкция)
# логическое умножение
# возвращает True только тогда, когда оба значения True
res = var_1 and var_2

# оператор "ИЛИ" (OR, операция дизъюнкция)
# логическое сложение
# возвращает False только тогда, когда оба значения False
res = var_1 or var_2

# отступы в python очень важны
# по отступам интерпретатор ориентируется во вложенности кода
# Tab - переменные курсора вправо на один отступ
# Backspace либо Shift + Tab - перемещение курсоа=ра влево на один отступ

# условные операции
a  = 5

# оператор if (если)
# if a == 0:
    # print('равно 0')

condition = a < 5

# if condition:
    # print('меньше 5')

# оператор else (иначе)
a = 10

# if a <= 10:
#     res = "hello!"
# else:
#     res = "bye-bye!"

# print (res)

# оператор elif (else if)
a = 0

# if a > 0:
#     res = "больше нуля"
# elif a < 0:
#     res = "меньше нуля"
# else:
#     res = "равно нулю"

char = "А"

if char == "A":
    res = "буква А"
elif char == "B":
    res = "буква В"
elif char == "c":
    res = "буква С"
else:
    res = "другой символ"

print(res)