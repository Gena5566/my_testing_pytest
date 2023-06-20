from my_function import is_even, double, sorted_numbers, math_pi, math_sqrt,math_pow
from my_function import math_hypot
import math

# функция filter
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-1) == False

def test_filter_even_numbers():
    numbers_is_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = filter(is_even, numbers_is_even)
    assert list(filtered_numbers) == [2, 4, 6, 8, 10]

# функция map
def test_map_double():
    numbers = [1, 2, 3, 4, 5]
    result = map(double, numbers)
    assert list(result) == [2, 4, 6, 8, 10]

# функция sorted
def test_sorted_numbers():
    numbers = [5, 2, 8, 1, 9]
    sorted_numbers = sorted(numbers)
    assert list(sorted_numbers) == [1, 2, 5, 8, 9]

# функция pi
def test_math_pi():
    assert math.pi == 3.141592653589793

# функция sqrt
def test_math_sqrt():
    numbers = [16, 25, 36, 49]
    result_sqrt = map(math_sqrt, numbers)
    assert list(result_sqrt) == [4.0, 5.0, 6.0, 7.0]

# Функция pow
def math_pow(base, exponent):
    # Возведение числа в степень
    return pow(base, exponent)

def test_math_pow():
    assert math_pow(2, 3) == 8
    assert math_pow(5, 0) == 1
    assert math_pow(10, -2) == 0.01
    assert math_pow(3, 4) == 81

def test_math_hypot():
    assert math_hypot(3,4) == 5



