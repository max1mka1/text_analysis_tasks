
'''
2. Напишите программу, которая считывает содержимое текстового файла 
и выводит на экран слова, сгруппированные по первой букве. Слова в 
файле разделены пробелами. Предложения разделены точками. 
Реализация должна быть основана на принципах ООП.
'''

import re

filename = "text.txt"                                        # Имя файла
f = open(filename, "r", encoding="utf-8")                    # encoding="utf-8" для кириллицы
text = f.read()                                              # Считываем файл
sentences = list(filter(None, re.split(r'[.]', text)))       # Разбиваем текст на предложения
words = []                                                   # Задаем список слов
for sent in sentences:                                       # Проходим по всем предложениям
    splited = re.split(r'[ ]', sent)
    all_words = list(filter(None, splited))                  # Разбиваем предложения на слова
    for word in all_words:                                   # Проходим по всем словам
        words.append(word.replace(",","").lower())           # Добавляем слово к списку, удаляем лишние запятые

for character in range(ord('а'), ord('я') + 1):
    char = chr(character)
    print('Слова на букву %s:' %char)
    for word in words:
        if re.match(r'\b[%s][а-яa-z]*\b' %char, word, re.IGNORECASE):
            print(word)
f.close()
