
'''
2. Напишите программу, которая считывает содержимое текстового файла
и выводит на экран слова, сгруппированные по первой букве. Слова в файле
разделены пробелами. Предложения разделены точками.
Реализация должна быть основана на принципах ООП.
'''

import re


class MainApp():

# функция инициализации - здесь считываем текст, и разбиваем по предложениям и словам
    def __init__(self):
        filename = "text.txt"                                        # Имя файла
        f = open(filename, "r", encoding="utf-8")                    # encoding="utf-8" для кириллицы
        text = f.read()                                              # Считываем файл
        self.sentences = list(filter(None, re.split(r'[.]', text)))  # Разбиваем текст на предложения
        self.words = []                                              # Задаем список слов
        for sent in self.sentences:                                  # Проходим по всем предложениям
            splited = re.split(r'[ ]', sent)
            words = list(filter(None, splited))                      # Разбиваем предложения на слова
            for word in words:                                       # Проходим по всем словам
                self.words.append(word.replace(",","").lower())      # Добавляем слово к списку слов self.words
        f.close()


    def Avg_length_of_words(self, words):                            # words это слова из __init__
        for character in range(ord('а'), ord('я') + 1):              # Проход по всем буквам алфавита
            char = chr(character)
            print('Слова на букву %s:' % char)
            for word in words:                                       # Проход по всем словам
                if re.match(r'\b[%s][а-я]*\b' % char, word, re.IGNORECASE):
                    print(word)


if __name__ == "__main__":
    app = MainApp()
    app.Avg_length_of_words(app.words)           # Передаем в качестве аргумента words список предложений self.words, создаваемый при инициализации init
