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

def percentage(a, b):
    return (a * b) / 100

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Корни уравнения: x1 = {root1}, x2 = {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Уравнение имеет один корень: x = {root}"
    else:
        return "Корней нет (дискриминант меньше нуля)"

print("1.+ ")
print("2. -")
print("3. *")
print("4. /")
print("5.  √")
print("6. ^2")
print("7. ^3")
print("8. %")
print("9. Решение уравнения (ax^2 + bx + c = 0)")

choice = input("Введите номер операции (1/2/3/4/5/6/7/8/9): ")

if choice in ['1', '2', '3', '4']:
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
elif choice == '5':
    x = float(input("Введите число для вычисления квадратного корня: "))
    print(f"Квадратный корень из {x} = {sqrt(x)}")
elif choice == '6':
    x = float(input("Введите число для возведения в квадрат: "))
    print(f"{x} ^ 2 = {power(x, 2)}")
elif choice == '7':
    x = float(input("Введите число для возведения в третью степень: "))
    print(f"{x} ^ 3 = {cube(x)}")
elif choice == '8':
    a = float(input("Введите число: "))
    b = float(input("Введите процент: "))
    print(f"{b}% от {a} = {percentage(a, b)}")
elif choice == '9':
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    print(solve_quadratic(a, b, c))
else:
    print("Неверный ввод")
