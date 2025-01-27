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

print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Квадратный корень")

choice = input("Введите номер операции (1/2/3/4/5): ")
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


else:
    print("Неверный ввод")