# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random

print("\n")
size = random.randint(10,20)
coins = [random.randint(0,1) for i in range(size)]
heads = 0
tails = 0

for i in range(size):
    if coins[i] == 1:
        tails += 1
    print(coins[i], end=" ")

print("\n")

heads = size - tails

if heads > tails or heads == tails:
    print(f"Всего монет {size} из них нужно перевернуть {tails} лежащих решкой (1) вверх")
else:
    print(f"Всего монет {size} из них нужно перевернуть {heads} лежащих гербом (0) вверх")