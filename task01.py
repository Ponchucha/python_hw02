
# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет,
# которые нужно перевернуть

import random
coins = int(input("Введите количество монеток: "))
side = 0
tail_count = 0
head_count = 0

for i in range(coins):
    side = random.randint(0, 1)
    if side == 0:
        tail_count += 1
        print("Решка")
    else:
        head_count += 1
        print("Орёл")

print(f"Чтобы все монетки лежали одной стороной, нужно перевернуть {tail_count if tail_count<head_count else head_count} штуки")
