#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # добавлено для квадратного корня

def add(a, b):
    """
    Складывает два числа.
    
    Args:
        a (float): Первое слагаемое
        b (float): Второе слагаемое
        
    Returns:
        float: Сумма a и b
        
    Example:
        >>> add(5, 3)
        8
    """
    return a + b

def subtract(a, b):
    """
    Вычитает второе число из первого.
    
    Args:
        a (float): Уменьшаемое
        b (float): Вычитаемое
        
    Returns:
        float: Разность a и b
        
    Example:
        >>> subtract(10, 4)
        6
    """
    return a - b

def multiply(a, b):
    """
    Умножает два числа.
    
    Args:
        a (float): Первый множитель
        b (float): Второй множитель
        
    Returns:
        float: Произведение a и b
        
    Example:
        >>> multiply(6, 7)
        42
    """
    return a * b

def divide(a, b):
    """
    Делит первое число на второе.
    
    Args:
        a (float): Делимое
        b (float): Делитель
        
    Returns:
        float or str: Результат деления или сообщение об ошибке
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 0)
        'Ошибка: деление на ноль!'
    """
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    """
    Возводит число в степень.
    
    Args:
        a (float): Основание
        b (float): Показатель степени
        
    Returns:
        float: Результат возведения в степень
        
    Example:
        >>> power(2, 3)
        8
    """
    return a ** b

def mod(a, b):
    """
    Возвращает остаток от деления.
    
    Args:
        a (float): Делимое
        b (float): Делитель
        
    Returns:
        float or str: Остаток от деления или сообщение об ошибке
        
    Example:
        >>> mod(10, 3)
        1
        >>> mod(10, 0)
        'Ошибка: деление на ноль!'
    """
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a % b

def square_root(a):
    """
    Вычисляет квадратный корень числа.
    
    Args:
        a (float): Число для извлечения корня
        
    Returns:
        float or str: Квадратный корень или сообщение об ошибке
        
    Example:
        >>> square_root(16)
        4.0
        >>> square_root(-4)
        'Ошибка: нельзя извлечь корень из отрицательного числа!'
    """
    if a < 0:
        return "Ошибка: нельзя извлечь корень из отрицательного числа!"
    return math.sqrt(a)

def calculate():
    """
    Основная функция калькулятора с пользовательским интерфейсом.
    
    Выводит меню, получает ввод от пользователя и выполняет выбранную операцию.
    """
    print("Простой калькулятор v1.0")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Остаток от деления")
    print("7. Квадратный корень")
    
    choice = input("Выберите операцию: ")
    
    try:
        a = float(input("Введите первое число: "))
        # Для квадратного корня нужно только одно число
        if choice != "7":
            b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите числа!")
        return
    
    if choice == "1":
        print(f"Результат: {add(a, b)}")
    elif choice == "2":
        print(f"Результат: {subtract(a, b)}")
    elif choice == "3":
        print(f"Результат: {multiply(a, b)}")
    elif choice == "4":
        print(f"Результат: {divide(a, b)}")
    elif choice == "5":
        print(f"Результат: {power(a, b)}")
    elif choice == "6":
        print(f"Результат: {mod(a, b)}")
    elif choice == "7":
        print(f"Результат: {square_root(a)}")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    calculate()
