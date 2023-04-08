"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""
import random


def operation(array, numRow, numCol):
    # print(array)
    # print(numRow ,numCol)
    x = array[numRow-1][numCol-1]
    # print(x)
    return x

def print_operation_table(operation, num_rows=6, num_columns=6):
    numRow = int(input("Enter element's row: "))
    numCol = int(input("Enter element's column: "))
    array = [[0 for j in range(num_columns)] for j in range(num_rows)]
    header = []
    for k in range(0,num_columns):
        header.append(k+1)
    print(0, header)
    print("")
    for i in range(num_rows):
        for j in range(num_columns -1):
            array[i][j] = random.randint(0,100)
        print(i+1, array[i])
    return operation(array,numRow,numCol)


print(print_operation_table(operation))