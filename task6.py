from itertools import cycle, count

for i in count(int(input('Введи начальное число: '))):
	print(i)


a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

cyc = cycle(a)

end = ''
while end != 'q':
	print(next(cyc), end='')
	end = input().lower()