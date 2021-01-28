with open("for_task2.txt") as f:
    a = f.readlines()
    print(f"кол-во строк: {len(a)}")
    for i in range(len(a)):
        print(f'кол-во символов: {i + 1}-ой строки {len(a[i])}')
    a = f.seek(0)
    a = f.read()
    a = a.split()
    print(f'Общее количество слов: {len(a)}')