import email

city_a = ('Moscow', 10)
city_b = ('Saint Petersburg', 644)
name1, km1 = city_a
name2, km2 = city_b
distance = km2 - km1
print(f'From: {name1}')
print(f'To: {name2}')
print(f'Distance: {distance} km')

print(7- (-8 - -2))

one = "Spencer"
two = "Kristina"
three = "Martina"

# BEGIN (write your solution here)
print(f'{one[1]}{three[2]}{two[2]}{two[6]}{two[4]}')
# END

print(int(3.99))

temperature = 36.6

# BEGIN (write your solution here)
temp_int = int(temperature)
temp_str = str(temp_int)
print(temp_int)
print(temp_str)
print(f'{temp_str} °C')
# END

text = 'Hello!'
x = len(text)
print(x)

distance = 450        # расстояние, км
fuel_consumption = 8.4  # расход топлива, л/100 км
fuel_price = 64.2     # цена топлива, руб./литр
passengers = 4        # количество пассажиров

# BEGIN (write your solution here)
print(round(distance / 100 * fuel_consumption, 1))
print(round(distance / 100 * fuel_consumption * fuel_price, 2))
print(round(distance / 100 * fuel_consumption * fuel_price / 4))
# END

text = "Hello, Python!"

# BEGIN (write your solution here)
print(f'First: {text[0]}\nLast: {text[-1]}')
# END

# imports are studied on Hexlet
from random import random

# BEGIN (write your solution here)
print(round(random() * 10))
# END

text = "the QUICK brown FOX jumps OVER the lazy DOG"

# BEGIN (write your solution here)
text_low = text.lower()
print(text_low)
# END

text = "log \t\n loading\t\n done"

# BEGIN (write your solution here)
print(len(text[4:15].strip()))
# END

# name = str(input("Input your name: "))
# def say_hello(name):
#     print(f'Hello, {name}!')
#
# say_hello(name)

def say_hello():
    print('Hello, World!')

say_hello()


def truncate(text, length):
# BEGIN (write your solution here)
    new_text = f'{text[:length]}...'
    print(new_text)
    return new_text
# END

truncate('hexlet', 2)

text = 'it works!'
truncate(text, 4)

def get_hidden_card(card_number, hidden=4, symbol="*"):
    hidden_card = symbol * hidden + card_number[-4:]
    return(hidden_card)

card_number = '2034399002121100'
get_hidden_card(card_number) # ****1100
get_hidden_card(card_number, 1) # *1100

# Именнованные аргументы
def trim_and_repeat(text, offset=0, repetitions=1):
    new_text = text[offset:] * repetitions
    return(new_text)

text = 'python'

trim_and_repeat(text, offset=3, repetitions=2)
trim_and_repeat(text, repetitions=3)
trim_and_repeat(text)

# Аннотация типов
def add(a: int, b: int) -> int:
    return(a + b)

print(add(4, 7))

def word_multiply(text: str, times: int) -> str:
    return text * times

text = 'python'
print(word_multiply(text, 2)) # => pythonpython
print(word_multiply(text, 0)) # =>

#Модули
import math


def amount_per_person(total: float, people: int, tip_percent: int) -> int:
# BEGIN (write your solution here)
    per_person = ((total + (total * tip_percent / 100)) / people)
    return math.ceil(per_person)
# END

amount_per_person(300, 4, 20)
amount_per_person(350, 3, 10)

import random
def generate_pin() -> int:
    x1 = random.randint(0, 9)
    x2 = random.randint(0, 9)
    x3 = random.randint(0, 9)
    x4 = random.randint(0, 9)
    return(f'{x1}{x2}{x3}{x4}')

#Логический тип
def is_pensioner(age: int) -> bool:
    return age >= 60

# print(is_pensioner(59))

# Сравнение строк
# print("hello".startswith("he"))   # True — строка начинается с "he"
# print("hello".endswith("lo"))     # True — строка заканчивается на "lo"
#
# print("123".isdigit())            # True — все символы являются цифрами
# print("abc".isalpha())            # True — все символы являются буквами
# print("abc123".isalnum())         # True — строка состоит только из букв и цифр
#
# print("   ".isspace())            # True — строка содержит только пробелы
# print("Hello".islower())          # False — не все символы в нижнем регистре
# print("HELLO".isupper())          # True — все символы в верхнем регистре
# print("Title Case".istitle())     # True — каждое слово начинается с заглавной буквы

def is_long_word(password: str) -> bool:
    return len(password) > 5

# print(is_long_word("appl"))

# Комбинирование операций и функций
def is_international_phone(phone_number: str) -> bool:
    first_number = phone_number[0]
    return first_number == "+"

# print(is_international_phone("89990764162"))

# Логические операции
def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# print(is_leap_year(2100))

# Отрицание
def is_palindrome(word: str) -> bool:
    new_word = word.lower()
    return new_word == new_word[::-1]

def is_not_palindrome(word: str) -> bool:
    return not is_palindrome(word)

# print(is_not_palindrome('Шалаш'))

# Результат логических выражений
def string_or_not(text: str) -> str:
    return isinstance(text, str) and 'yes' or 'no'

# print(string_or_not(10))

# Конфигурация if
def guess_number(number: int) -> str:
    return number==42 and 'You win!' or 'Try again!'

# print(guess_number(42))

def guess_number1(number: int) -> str:
    if number == 42:
        return 'You win!'
    return 'Try again!'

# print(guess_number1(142))

# Условная конструкция else
def normalize_url(adress: str) -> str:
    if adress[:8] == 'https://':
        return(adress)
    if adress[:7] == 'http://':
        return(f'{adress[:4]}s{adress[4:]}')
    else:
        return(f'https://{adress}')
    return
# print(normalize_url('https://ya.ru'))
# print(normalize_url('google.com'))
# print(normalize_url('http://ai.fi'))

# Условные конструкции if, else, elif
def get_traffic_light_action(color: str) -> str:
    if color == 'green':
        return('go')
    elif color == 'yellow':
        return('slow down')
    elif color == 'red':
        return('stop')
    else:
        return('unknown')

print(get_traffic_light_action('blue'))

# Тернарный оператор
def flip_flop(text: str) -> str:
    if text == 'flip':
        return 'flop'
    else:
        return 'flip'
    return

def flip_flop(text: str) -> str:
    return 'flip' if text == 'flop' else 'flop'

# print(flip_flop('flip'))

# Оператор MATCH
def calculate_delivery_cost(country: str, weight: float) -> float:
    match country:
        case 'canada':
            return 600 if weight <= 1 else 900
        case 'usa':
            return 800 if weight <= 1 else 1200
        case 'germany':
            return 700 if weight <= 1 else 1000
        case '':
            return 'None'
    return

# print(calculate_delivery_cost('russia', 2131.645))

# Цикл While
# counter = 0
# while counter < 5:
#     print("Hello!")
#     counter = counter + 1

def print_countdown(count: int) -> int:
    i = count
    while i > 0:
        print(i)
        i = i - 1
    print('Go!')

# print(print_countdown(5))

# Условия внутри цикла
def count_hashtags(text: str) -> int:
    i = 0
    x = len(text)
    a = 0
    while a < x:
        if text[a] == '#':
            i = i + 1
            a = a + 1
        else:
            a = a + 1
    return(i)

# print(count_hashtags('H#el#l#####o'))

# Агрегация данных (числа)
def calculate_electricity_bill(kwatt: int) -> int:
    i = 1
    sum = 0
    while i <= kwatt:
        if i <= 100:
            sum = sum + 5
        elif 100 < i <= 200:
            sum = sum + 7
        elif i > 200:
            sum = sum + 10
        i = i + 1
    return sum

# print(calculate_electricity_bill(80))

# Агрегация данных (строки)
def sanitize_phone_number(number: str) -> str:
    start_num = ''
    i = 0
    while i < len(number):
        if number[i:i+1] == "+":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "0":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "1":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "2":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "3":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "4":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "5":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "6":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "7":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "8":
            start_num = start_num + number[i:i+1]
        elif number[i:i+1] == "9":
            start_num = start_num + number[i:i+1]
        i = i + 1
    return start_num

def sanitize_phone_number1(phone: str) -> str:
    i = 0
    start_num = ''
    while i < len(phone):
        letter = phone[i]
        if letter not in " ()-":
            start_num = start_num + letter
        i = i + 1
    return start_num

# print(sanitize_phone_number1('+7 (999) 123-45-67'))

# Обход строк
def mask_card_number(card_number: str) -> str:
    new_num = ''
    i = 0
    while i < (len(card_number) - 4):
        new_num = new_num + '*'
        i = i + 1
    new_num = new_num + card_number[i:]
    return new_num

# print(mask_card_number("12345678"))

def build_progress_bar(step: int, count: int) -> str:
    result = ''
    i = 0
    while i < count:
        if i < step:
            result += '#'
        else:
            result += '-'
        i = i + 1
    return result

# print(build_progress_bar(5, 5))


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True

# print(is_prime(1))

def has_at_symbol(text: str) -> bool:
    i = 0
    char = '@'
    while i < len(text):
        char = text[i]
        if char == '@':
            return True
        i += 1
    return False

# print(has_at_symbol('support@example.com'))

# Цикл for
def normalize_filename(text: str) -> str:
    new_name = ''
    for char in text:
        if char == ' ':
            new_name = new_name + '_'
        else:
            new_name = new_name + char
    return new_name

# print(normalize_filename('my photo.png'))
# print(normalize_filename('final report.pdf'))
# print(normalize_filename('already_ready.txt'))

# Цикл for и функция range

def fizzbuzz(numbers: int) -> str:
    result = ''
    for number in range(1, numbers + 1):
        if number % 3 == 0 and number % 5 == 0:
            result += 'FizzBuzz'
        elif number % 3 == 0:
            result += 'Fizz'
        elif number % 5 == 0:
            result += 'Buzz'
        else:
            result += str(number)
        if number != numbers:
            result += ' '
    return result

# print(fizzbuzz(15))

def compress(string: str) -> str:
    if not string:
        return ""

    result = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += string[i - 1]
            if count > 1:
                result += str(count)
            count = 1

    result += string[-1]
    if count > 1:
        result += str(count)

    return result

# print(compress("aaabcccc"))