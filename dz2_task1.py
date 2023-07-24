# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два 
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random

print("\n")
x_num = random.randint(1, 1000)
y_num = random.randint(1, 1000)
i=1
summ = x_num + y_num
mult = x_num * y_num
sum = summ
print(f"Сумма X и Y = {summ}")
print(f"Произведение X и Y = {mult}")
for i in range(summ):
    if i * sum == mult:
        print(f"X = {i}")
        print(f"Y = {sum}")
        break
    i += 1
    sum -= 1