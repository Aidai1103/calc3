import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"
    
def sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Ошибка: нельзя вычислить корень из отрицательного числа" 

def power(x, y):
    return x ** y
def cube(x):
    return x ** 3
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Квадратный корень")
print("6. Возведение в степень")
print("7. Возведение в третью степень")
choice = input("Введите номер операции (1/2/3/4/5/6/7): ")
if choice in ['1', '2', '3', '4', '6']:
 x = float(input("Введите первое число: "))
 y = float(input("Введите второе число: "))

if choice == '1':
    print(f"{x} + {y} = {add(x, y)}")
elif choice == '2':
    print(f"{x} - {y} = {subtract(x, y)}")
elif choice == '3':
    print(f"{x} * {y} = {multiply(x, y)}")
elif choice == '4':
    print(f"{x} / {y} = {divide(x, y)}")
elif choice == '6':
        print(f"{x} ^ {y} = {power(x, y)}")

elif choice == '5':
    x = float(input("Введите число для вычисления квадратного корня: "))
    print(f"Квадратный корень из {x} = {sqrt(x)}")
elif choice == '7':
    x = float(input("Введите число для возведения в третью степень: "))
    print(f"{x} ^ 3 = {cube(x)}")

else:
    print("Неверный ввод")