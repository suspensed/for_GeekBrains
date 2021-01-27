import sys, time

hours, money_per_hour, prize = sys.argv[1:]
print(f'Ваша зарплата: {int(hours) * int(money_per_hour) + int(prize)} ')