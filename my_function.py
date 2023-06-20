import math
# функция filter
def is_even(num):
    return num % 2 == 0

# Последовательность чисел
numbers_is_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Фильтрация четных чисел
filtered_numbers = filter(is_even, numbers_is_even)

# Вывод результатов
print(list(filtered_numbers))

# функция map
def double(num):
    return num * 2

# Последовательность чисел
numbers_num = [1, 2, 3, 4, 5]

# Применение функции double к каждому элементу
result = map(double, numbers_num)

# Вывод результатов
print(list(result))

# функция sorted
def sorted_numbers(num):
    return sorted(num)
# Сортировка списка чисел по возрастанию
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(list(sorted_numbers))

# функция pi
def math_pi():
    return math.pi
print(math.pi)

# функция sqrt
def math_sqrt(num):
    return math.sqrt(num)
numbers = [16, 25, 36, 49]
# Применение функции math_sqrt к каждому элементу
result_sqrt = map(math_sqrt, numbers)
# Вывод результатов
print(list(result_sqrt))

# Функция pow
def math_pow(base, exponent):
    # Возведение числа в степень
    return pow(base, exponent)
base = [1, 2, 3, 4, 5]
exponent = 3
# Применение функции к каждому элементу
result = map(lambda x: math_pow(x, exponent), base)
# Вывод результатов
print(list(result))

# Функция   hypot
def math_hypot(a,b):
    # Вычисление гипотенузы прямоугольного треугольника
    return math.hypot(a, b)
print(math_hypot(3,4))







