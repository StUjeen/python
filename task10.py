'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''
import random

n = int(input("Enter n: "))
coinSet = []
i=0
for i in range(n):
    toss = (random.randint(0,1))
    coinSet.append(toss)
#    print(f"i = {i}")
print(f"coinSet = {coinSet}, {len(coinSet)}")

countAvers = 0
countRevers = 0
lenght = len(coinSet)
j = 0
while j < lenght:
#    print(f"j = {j}, coinSet[j] = {coinSet[j]}")
    if coinSet[j] == 1:
        countAvers += 1
#        print(f"countAversIter = {countAvers}")
    else:
        countRevers += 1
#        print(f"countReversIter = {countRevers}")
    j += 1
if countAvers <= countRevers:
    print(f"turn {countAvers} time(s)")
else:
    print(f"turn  {countRevers} time(s)")

#print(f"countAvers = {countAvers}")
#print(f"countRevers= {countRevers}")
