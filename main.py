#1-я задание

number = 2234567

a = 0
b = 0

num_1 = number // 1000000
num_2 = number // 100000 % 10
num_3 = number // 10000 % 10
num_4 = number // 1000 % 10
num_5 = number // 100 % 10
num_6 = number // 10 % 10
num_7 = number % 10
i = 0
while i <= 7:
    if i % 2 == 0:
        a += 1
    else:
        b += 1
i += 1
if a > b:
    print(1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7)



#2-е задание

text = str(input('Введите текст: '))
gl = 0
sogl = 0
i = 0
for i in text:
    if i in 'oaeiu':
        gl += 1
    else:
        sogl += 1
if gl != sogl:
    print("Гласных: ", gl, "Согласных: ", sogl)
else:
    for i in text:
        if i in 'oaeiu':
            print(i)

#3-е задание:


import random
i = 1
result = 0
while i < 7:

    num_1 = int(input('Введите число от 1 до 20: '))
    num_2 = int(input('Введите число от 1 до 20: '))

    n_1 = random.randint(1, 20)
    n_2 = random.randint(1, 20)
    print("Рандомные числа: ", n_1,",", n_2)


    if num_1 > n_1 and num_2 > n_2:
        result += 1
    i += 1
print(result)


#5-е задание:


list = [88, 'retro', 1989, 'party']
i = 0
while i < len(list):
    if type(list[i]) == int:
        print(list[i])
    i += 1
