"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  
"""

# phrase = input("Enter your text: ")
phrase = "пара-ра-рам"

def findRhyme (text):
    phraseList = text.split(" ") #разделяем текст на фразы, получаем список
    symbols = 'аеиоуыэюя' #задаем набор гласных для дальнейшего сравнения
    temp = list()
    for i in range(len(phraseList)): # перебираем каждую фразу
        # print(phraseList[i], " ", range(len(phraseList[i]))) ### селф-чек
        count = 0
        for j in range(len(phraseList[i])): # перебираем каждое слово во фразе
            if phraseList[i][j] in symbols:
                count += 1
        temp.append(count)
    
    result = str()
    for k in range(len(temp)): # сравниваем количество гласных в каждой фразе
        if len(temp)-1 == 0 or (k < len(temp)-1 and temp[k] != temp[k + 1]): 
            return "Пам парам"
        elif k < len(temp)-1 and temp[k] == temp[k + 1]: 
            result = "Парам пам-пам"
        else: return result

print(findRhyme(phrase))