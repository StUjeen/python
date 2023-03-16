'''
 Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
******** Рассмотрите вариант разделения на правую и левую часть произвольно, но не меняя порядок цифр.
'''
number = input("Enter 6 digit number: ")
while len(number) != 6:
    number = input("Enter 6 digit number: ")
else:
    firstHalf = str(number)[:3]
    secondHalf = str(number)[-3:]

firstSum = int(str(firstHalf[0])) + int(str(firstHalf[1])) + int(str(firstHalf[2]))

secondSum = int(str(secondHalf[0])) + int(str(secondHalf[1])) + int(str(secondHalf[2]))

if firstSum == secondSum:
    print(f"{number} -> yes :)")
else:
    print(f"{number} -> no :(")