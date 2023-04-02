"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

start = int(input("Enter the first element: "))
diff = int(input("Enter step length: "))
lenght = int(input("Enter number of elements: "))

def progression(start, diff, lenght):
    row = list()
    for i in range(lenght):
        row.append(start + i * diff)
    print(row)

progression(start, diff, lenght)
