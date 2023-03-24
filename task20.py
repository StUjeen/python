'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 

А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
'''

word = input("Enter your word: ")
sequence = {
    "AEIOULNSTRАВЕИНОРСТ" : 1
    ,"DGДКЛМПУ" : 2
    ,"BCMPБГЁЬЯ" : 3
    ,"FHVWYЙЫ" : 4
    ,"KЖЗХЦЧ" : 5
    ,"JXШЭЮ" : 8
    ,"QZФЩЪ" : 10
}
keys = list(sequence.keys())
count = 0
# print(f"lenSeq = {len(sequence)}, lenWord = {len(word)}")
for i in range(len(word)):
    # print(i)
    j = 0
    while j < len(sequence): 
        # print(j)
        for k in range(len(keys[j])):
            temp = keys[j]
            if word[i].upper() == temp[k]:
                count += sequence[keys[j]]
            # print(f"k = {k} ,keys[j] = {keys[j]}, temp[k] = {temp[k]}")
        j += 1

print(word)
print(count)