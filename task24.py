"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
import random
import math

# grow bushes
bushNumber = abs(int(input("Enter number of bushes: ")))
harvestBerries = list()
if bushNumber == 0:
    harvestBerries.append(0)
else:
    bushBerries = list()
    for i in range(bushNumber):
        bushBerries.append(random.randint(0, 1000))
    print(f"number of bushes = {bushNumber}, berries per bush = {bushBerries}")
# harvest berries
    if bushNumber == 1:
        harvestBerries.append(bushBerries[0])
    else:
        j = 0
        while j < bushNumber:
            if bushNumber > 1 and j == 0:
                harvestBerries.append(bushBerries[j] + bushBerries[j+1])
            elif  bushNumber > 1 and j == bushNumber - 1:
                harvestBerries.append(bushBerries[j] + bushBerries[j-1])
            else:
                harvestBerries.append(bushBerries[j] + bushBerries[j+1] + bushBerries[j-1])
            j += 1
        print(f"harvested = {harvestBerries}")
# calculate the best harvested bush
if bushNumber == 0:
    print("No bushes no berries :(")
elif bushNumber == 1:
    print(f"The only bush has {harvestBerries} :(")        
else:    
    max = harvestBerries[0]
    for r in range(len(harvestBerries)):
            if max > harvestBerries[r]:
                continue
            else:
                max = harvestBerries[r]
                bestBushNumber = r + 1 
# show results
    print(f"{max} berries in front of bush number {bestBushNumber}")

