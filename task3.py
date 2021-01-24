def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b

    elif a > b and a < c:
        return a + c

    else:
        return b + c

print(my_func(10, 12, 11))


