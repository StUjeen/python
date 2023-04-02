'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19]
'''

initRow = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
start = int(input("Enter min value: "))
end = int(input("Enter max value: "))

def indexRow(initRow, start, end):
    resultList = list()
    for i in range(len(initRow)):
        if initRow[i] >=start and initRow[i] <= end:
            resultList.append(i)
        else: continue
    print(resultList)

indexRow(initRow, start, end)