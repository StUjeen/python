'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
import random

n = int(input("Enter N: "))
x = int(input("Enter X: "))
array = [0]
i = 0
for i in range(n):
    rand = random.randint(0, 100)
    array.append(rand)

count = 0
for i in range(len(array)):
    if array[i] == x:
        count += 1
    else:
        continue

print(array)
print(x)
print(f"-> {count}")