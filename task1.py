with open('test.txt', 'w') as my_f:
    line = input('Введите текст \n')
    while line:
        my_f.writelines(line)
        line = input('Введите текст \n')
        if not line:
            break


with open('test.txt', 'r') as my_f:
    content = my_f.readlines()
    print(content)
