"""
Тесты для калькулятора.
Проверяем, что все функции работают правильно.
"""

import math
import pytest
from calculator import (
    add, subtract, multiply, divide,
    power, mod, square_root
)

# Тесты для сложения
def test_add_positive():
    """Тест сложения положительных чисел"""
    assert add(2, 3) == 5
    assert add(10, 5) == 15

def test_add_negative():
    """Тест сложения отрицательных чисел"""
    assert add(-2, -3) == -5
    assert add(-5, 3) == -2

def test_add_float():
    """Тест сложения дробных чисел"""
    assert add(2.5, 3.1) == 5.6
    assert add(0.1, 0.2) == 0.3  # Проверка погрешности

# Тесты для вычитания
def test_subtract_positive():
    """Тест вычитания положительных чисел"""
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0

def test_subtract_negative():
    """Тест вычитания отрицательных чисел"""
    assert subtract(-5, -3) == -2
    assert subtract(-5, 3) == -8

# Тесты для умножения
def test_multiply_positive():
    """Тест умножения положительных чисел"""
    assert multiply(4, 5) == 20
    assert multiply(3, 7) == 21

def test_multiply_negative():
    """Тест умножения отрицательных чисел"""
    assert multiply(-4, 5) == -20
    assert multiply(-4, -5) == 20

# Тесты для деления
def test_divide_normal():
    """Тест обычного деления"""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Тест деления на ноль (должна быть ошибка)"""
    result = divide(10, 0)
    assert result == "Ошибка: деление на ноль!"

# Тесты для возведения в степень
def test_power_positive():
    """Тест возведения в положительную степень"""
    assert power(2, 3) == 8
    assert power(5, 2) == 25

def test_power_zero():
    """Тест возведения в нулевую степень"""
    assert power(2, 0) == 1
    assert power(10, 0) == 1

def test_power_negative():
    """Тест возведения в отрицательную степень"""
    assert power(2, -1) == 0.5
    assert abs(power(2, -2) - 0.25) < 0.0001

# Тесты для остатка от деления
def test_mod_normal():
    """Тест остатка от деления"""
    assert mod(10, 3) == 1
    assert mod(17, 5) == 2

def test_mod_by_zero():
    """Тест остатка от деления на ноль"""
    result = mod(10, 0)
    assert result == "Ошибка: деление на ноль!"

# Тесты для квадратного корня
def test_square_root_normal():
    """Тест квадратного корня из положительных чисел"""
    assert square_root(16) == 4
    assert square_root(25) == 5
    assert square_root(2) == math.sqrt(2)

def test_square_root_zero():
    """Тест квадратного корня из нуля"""
    assert square_root(0) == 0

def test_square_root_negative():
    """Тест квадратного корня из отрицательного числа"""
    result = square_root(-4)
    assert result == "Ошибка: нельзя извлечь корень из отрицательного числа!"

# Тест для неправильного ввода (проверяем функцию calculate не будем, она сложная)

if __name__ == "__main__":
    print("Запуск тестов...")
    pytest.main(["-v", __file__])
