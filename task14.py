'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
import math

n = abs(int(input("Enter N: ")))
twoPowers = []
i = 1
for i in range(n):
    if (2 ** i) > n:
        break
    elif (i == 0):
        continue
    else:
        twoPowers.append(i)

print(f"n = {n}, set of powers = {twoPowers}")

