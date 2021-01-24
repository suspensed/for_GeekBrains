# Первый способ
def my_func(x, y):
    return x**y

print(my_func(2, -3))

# Второй способ
def my_second_func(x, y):
    if y < 0:
        x = 1.0 / x
        y = -y
    res = 1
    while y > 0:
        res = res * x
        y = y - 1 
    return res
    
print(my_second_func(2, -3))
