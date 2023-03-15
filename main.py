#Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

n = input("Введите число: ")
partOne = n + ' ->'
#print(type(partOne))
n = n.replace('.','')
n = int(n)
inputNumber = n
sum = 0
partThree = str()
i = len(str(n))
while n != 0:
    lastNumber = n % 10
#    print(f"lastNumber = {lastNumber}")
    n //= 10
#    print(f"n = {n}")
#    print(lastNumber, type(lastNumber))
    sum += lastNumber
#    print(sum)

#print(i)
while i > 0:
    if i == 1:
        partThree += str(inputNumber % 10)
#        print(str(inputNumber // 10**(i-1))[-1])
        i = 0
    else:
        partThree += str(inputNumber // 10**(i-1))[-1] + ' + '
#        print(str(inputNumber // 10**(i-1))[-1])
        i -= 1
print(f"{partOne} {sum} ({partThree})")