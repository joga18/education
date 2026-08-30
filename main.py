#Изучение питона с гитхаба https://github.com/ipzxc191/python-backend-course/blob/main/python-base/lesson02.md

#Урок 1
#Урок 2 Операции с числами: сложение, вычитание, умножение, деление
x = 10 // 3
y = 10 % 3
print(type(8/2))
#Урок 3
#abs(x): возвращает абсолютное значение числа x.
#round(x): округляет число x до ближайшего целого значения.
#max(x1, x2, ...): возвращает наибольшее значение из переданных аргументов.
#min(x1, x2, ...): возвращает наименьшее значение из переданных аргументов.
#pow(x, y): возвращает значение x в степени y.
#sum(iterable): возвращает сумму всех элементов в итерируемом объекте.
#math.sqrt(x): возвращает квадратный корень числа x.
import math
x = math.sqrt(121)
print(x)

#math.pow(x, y): возвращает значение x в степени y.
y = math.pow(2, 5)
print(y)

#math.ceil(x): округляет число x вверх до ближайшего целого значения.
z = math.ceil(100/33)
print(z)

#math.floor(x): округляет число x вниз до ближайшего целого значения.
g = math.floor(15/4)
print(g)

#math.radians(x): преобразует угол из градусов в радианы.
x = math.radians(60)
print(x)

#math.sin(x), math.cos(x), math.tan(x): возвращают синус, косинус и тангенс угла x (в радианах).
x = math.sin(math.radians(60))
print(x)

#math.log(x, base): возвращает логарифм числа x по указанному основанию base.
y = math.log(9, 3)
print(y)

#math.log10(x): возвращает десятичный логарифм числа x.
u = math.log10(1000)
print(u)

#math.factorial(x): возвращает факториал числа x.
a = math.factorial(5)
print(a)

#Функция print() используется для вывода текста или значений переменных на экран.
#Она может принимать один или несколько аргументов, разделенных запятыми.
#Аргументы могут быть строками, числами или другими объектами, которые могут быть преобразованы в строку.
#Функция print() автоматически добавляет символ новой строки (\n) в конце вывода,
#но это поведение можно изменить с помощью аргументов end и sep.

x = 17
my_str = "Привет, мир!"
print(my_str)  # Выводит строку "Привет, мир!"
print(x)  # Выводит число 17
print("Значение переменной x:", x)  # Выводит значение переменной x

x = 17
my_str = "Привет, мир!"
# Выводит результат двух print в одну строку
print(my_str, end=' ')
print('Значение переменной x:', x, end=' ')

x = 17
my_str = "Привет, мир!"
# Выводит результат одного принта в нескольких строках
print(my_str, x, 'Такие дела...', sep='\n')

#Функция input() используется для получения ввода от пользователя.
# name = input("Введите свое имя: ")
# print("Привет, " + name + "!" )
#
# age = int(input("Введите свой возраст: "))
# print(f"Тебе {age}!")

# Задания
x = 2
y = 5
z = 12
print(x, y, z)
print(x, y, z, sep='\n')

x = "Привет,"
y = "Мир!"
print(x, end=' ')
print(y)

# x = input("Как тебя зовут?: ")
# y = input("Твоя любимая футбольная команда: ")
# z = input("В каком городе ты живешь?: ")
# print(f"{x}, {y}, {z}")

# d = int(input("Введите целое отрицательное число: "))
# print(abs(d))

a = 1
b = 3
c = -45
d = 12
e = 0
print(min(a,b,c,d,e))
print(max(a,b,c,d,e))

a = 3
b = 4
c = a**2 + b**2
print(math.sqrt(c))

# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# print(a**b)

a = 40
b = 5
c = 20
print(math.ceil((a+b)/c))

a = 20
b = 0.1
c = 500
print(c//(a-a*b))

# x1 = int(input("Введите координату x1:"))
# y1 = int(input("Введите координату y1:"))
# x2 = int(input("Введите координату x2:"))
# y2 = int(input("Введите координату y2:"))
# print(f"Расстояние между точками равно {math.sqrt((x1-x2)**2+(y1-y2)**2)}")

#Урок 4
# x = input('Введите первое число: ')
# y = input('Введите второе число: ')
# print(int(x) > int(y))

# text = input('Введите текст: ')
# print(str(text) != '')

# text = input('Введите текст: ')
# print(not str(text))

# x = input('Введите первое число: ')
# y = input('Введите второе число: ')
# z = input('Введите третье число: ')
# print(int(x) > 0 or int(y) > 0 or int(z) > 0)

# x = input('Введите первое число: ')
# print(int(x) % 2 == 0)

# a = float(input("Введите число: "))
# print(int(a) % 3 == 0)

# x = float(input("Введите стоимость книги: "))
# print(((x - int(x)) * 100) > 50)

# a = int(input("Введите первую сторону треугольника: "))
# b = int(input("Введите вторую сторону треугольника: "))
# c = int(input("Введите третью сторону треугольника: "))
# print (a + b > c and a + c > b and b + c > a)

# Урок 5 Введение в строки и операции над ними

char = 'z'
ascii_code = ord(char)
print(ascii_code)

symbol_a = chr(999)
print(symbol_a)

# x = input('Введите текст: ')
# y = input('Введите текст: ')
# print(x + ' ' + y)

s1 = "hello"
s2 = "python"
print(s1 * 2 + s2 * 3)

a = 12
b = 7
print('Переменная а = ' + str(a) + ', переменная b = ' + str(b))

# x = input('Введите текст: ')
# print(len(x))

s1 = "Hello, Python!"
print('Строка: ' + s1 + ' Длина строки: ' + str(len(s1)))

# x = input('Введите текст: ')
# print('Python' in x)

s1 = "str"
s2 = "secondstr"
print(s1 in s2)
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)

char1 = "a"
char2 = "z"
print('Коды: ' + char1 + ' = ' + str(ord(char1)) + ', ' + char2 + ' = ' + str(ord(char2)))

# Урок 6 Индексы и срезы строк
main_string = "Привет, мир!"
reversed_string = main_string[::-1]  # Получаем строку в обратном порядке "!рим ,тевирП"
substring1 = main_string[4:1:-1]  # Получаем подстроку "еви"
substring2 = main_string[::-2] # Получаем каждый второй символ в обратном порядке
substring3 = main_string[1:4:-1] # Получаем пустую строку
print("reversed_string: ", reversed_string)
print("substring1: ", substring1)
print("substring2: ", substring2)
print("substring3: ", substring3)

main_string = "Hello World!"
second_string = main_string[:-1] + "?"
print(main_string)
print(second_string)

# text = input('Введите текст: ')
# print(text)
# print(text[0], text[-1])
# print(text[0:4])
# print(text[-3:])
# print(text[::2])
# print('Python' in text)
# print(text[3:])
# print(text[:-6:-1])

# x = input('Введите текст: ')
# y = input('Введите текст: ')
# print(x[1::2] + ' ' + y[::2])

# x = input('Введите текст: ')
# y = input('Введите текст: ')
# print(y[:len(x)])

# Урок 7. Основные методы строк
# upper() - Возвращает строку с заглавными буквами.
# lower() - Возвращает строку с малыми буквами.
# capitalize() — Делает первую букву строки заглавной.
# title() — делает первую букву каждого слова заглавной.
# swapcase() — меняет регистр каждого символа (верхний на нижний и наоборот).
# count(sub) - Определяет число вхождений подстроки
# find(sub) - Возвращает индекс первого найденного вхождения sub
# ndex(sub) - Возвращает индекс первого найденного вхождения
# rfind(sub) - Возвращает индекс первого найденного вхождения при поиске справа.
# rindex(sub) — возвращает индекс последнего вхождения подстроки sub
# split() - Разбивает строку на подстроки и возвращает список
# join(iterable) - Метод объединяет элементы итерируемого объекта в одну строку
# partition(sep) — Метод возвращает кортеж, состоящий из трех элементов: части строки до разделителя
# replace(old, new) - Заменяет подстроку old на new. Метод может принимать третий аргумент — count
# strip() - Метод используется для удаления пробелов (или других символов) с начала и конца строки. Он может принимать один необязательный аргумент chars, который определяет, какие символы следует удалить: String.strip(chars).
# rjust(width) - Расширяет строку, добавляя символы слева.
# isalpha() - Определяет, состоит ли строка целиком из буквенных символов.
# isdigit() - Определяет, состоит ли строка целиком из цифр.
# isalnum() — Метод возвращает True, если все символы в строке являются алфавитно-цифровыми
# startswith(sub) - возвращает True, если строка начинается с указанной подстроки
# endswith(sub) - возвращает True, если строка заканчивается указанной подстрокой

# text = input('Введите текст: ')
# print(text.upper())
# print(text.strip())
# print(text.capitalize())
# print(text.replace('старый', 'новый'))
# print(text.count('-'))
# print(text.find('world'))
# print(text.replace('--', '-'))

# text = input('Введите текст: ')
# text = text.split()
# lenght = len(text)
# print(lenght)
# result = ';'.join(text)
# print(result)

# text = input('Введите текст: ')
# text = text.replace(',', '')
# text = text.split()
# print(text[:2])

text = input('Введите тектс: ')
text.rjust(4, '-')
print(text)