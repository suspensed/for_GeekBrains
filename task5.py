from functools import reduce

def func(x, y):
	return x * y

a = [i for i in range(100, 1001) if i % 2 == 0]

print(reduce(func, a))