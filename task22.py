"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
import random

def createSet(x):
    i = 0
    result = list()
    while i < x:
        if x <= 5:
            element = int(input("Enter next element: "))
            result.append(element)
        else:
            result.append(random.randint(1,100))
        i += 1
    return result
# define set One elements
print("Define set One:")
n = int(input("Enter lenght for the first set: "))
setOne = set(createSet(n))
print(f"your set One is defined: {setOne}")

# define set Two elements
print("Define set Two:")
m = int(input("Enter lenght for the second set: "))
setTwo = set(createSet(m))
print(f"your set Two is defined: {setTwo}")

# Intersection and sorting printed result
resultingSet = setOne.intersection(setTwo)
print(f"intersection -> {sorted(resultingSet)}")

