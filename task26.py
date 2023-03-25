"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""
import math
def aToPowerB(a,b):
    if b == 1:
        return a
    return a * aToPowerB(a, b-1)

a = abs(int(input("Enter A: ")))
b = abs(int(input("Enter B: ")))
print(f"A = {a}, B = {b} -> {aToPowerB(a,b)}")