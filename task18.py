'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

import random
import math
# input data
n = int(input("Enter N: "))
x = int(input("Enter X: "))
array = list()
# create array
for i in range(n):
    rand = random.randint(0, 100)
    array.append(rand)
# find the number
diff = abs(array[0] - x)
print(diff)
closest = array[i]
for i in range(n):
    if abs(array[i] - x) == 0:
        closest = array[i]
        break
    elif abs(array[i] - x) <= diff:
        diff = abs(array[i] - x)
        closest = array[i]

# print results
print(array)
print(x)
print(f"-> {closest}")