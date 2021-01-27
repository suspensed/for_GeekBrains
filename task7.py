from math import factorial
from itertools import count

def generator():
	for el in count(1):
		yield factorial(el)

x = 1 
for a in generator():
	print(f'Факториал: {x} {a}')
	if x == 15:
		break
	x += 1