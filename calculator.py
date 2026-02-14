#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел (a - b)"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел (a / b) с проверкой деления на ноль"""
    if b == 0:
        return "ОШИБКА: Деление на ноль невозможно!"
    return a / b

def get_number(prompt):
    """Получение числа от пользователя с обработкой ошибок"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите число (целое или дробное через точку).")

def print_menu():
    """Вывод меню с доступными операциями"""
    print("\n" + "="*40)
    print("            ПРОСТОЙ КАЛЬКУЛЯТОР")
    print("="*40)
    print("Доступные операции:")
    print("  1. Сложение (+)")
    print("  2. Вычитание (-)")
    print("  3. Умножение (*)")
    print("  4. Деление (/)")
    print("  5. Выход")
    print("="*40)

def main():
    """Основная функция программы"""
    while True:
        # Показываем меню
        print_menu()
        
        # Получаем выбор пользователя
        choice = input("Выберите операцию (1-5): ").strip()
        
        # Выход из программы
        if choice == '5':
            print("\nСпасибо за использование калькулятора! До свидания!")
            break
        
        # Проверка корректности выбора
        if choice not in ['1', '2', '3', '4']:
            print("\nОШИБКА: Неверный выбор! Пожалуйста, выберите 1-5.")
            continue
        
        # Получаем числа от пользователя
        print("\n" + "-"*20)
        print("Введите числа:")
        num1 = get_number("Первое число: ")
        num2 = get_number("Второе число: ")
        print("-"*20)
        
        # Выполняем выбранную операцию
        if choice == '1':
            result = add(num1, num2)
            print(f"\nРезультат: {num1} + {num2} = {result}")
        
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nРезультат: {num1} - {num2} = {result}")
        
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nРезультат: {num1} * {num2} = {result}")
        
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):  # Если это сообщение об ошибке
                print(f"\nРезультат: {result}")
            else:
                print(f"\nРезультат: {num1} / {num2} = {result}")
        
        # Ждем нажатия Enter перед продолжением
        input("\nНажмите Enter, чтобы продолжить...")

# Точка входа в программу
if __name__ == "__main__":
    main()
