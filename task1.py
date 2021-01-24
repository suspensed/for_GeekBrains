a = float(input())
b = float(input())

def division(a, b):
    try:
        print(a / b)

    except ZeroDivisionError:
        print('Деление на ноль')

division(a, b)
