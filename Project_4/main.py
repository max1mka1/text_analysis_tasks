
'''
4. Программа, которая извлекает из текстового файла все слова,
представляющие собой номера телефонов в двух форматах.
'''

import re


class MainApp():

# функция инициализации - здесь считываем текст, и разбиваем по предложениям и словам
    def __init__(self):
        filename = "text.txt"                                        # Имя файла
        f = open(filename, "r", encoding="utf-8")                    # Открываем файл в кодировке utf-8
        text = f.read()                                              # Создаем объект text с содержимым файла
        self.splited_text = re.split(" ", text)                      # Разделяем текст на слова, разделенные пробелом
        f.close()


    def Main_Task(self, splited_text):
        print('Список извлеченных из текста номеров:')
        for element in splited_text:
            result = re.match("\+7[0-9]{10}", element)      # Ищем совпадение номеров с +7
            result2 = re.match("8[0-9]{10}", element)       # Ищем совпадение номеров с 8
            if result:                                      # В случае совпадения печатаем
                print(result.group(0))
            elif result2:
                print(result2.group(0))


if __name__ == "__main__":
    app = MainApp()
    app.Main_Task(app.splited_text)                       # Выполняем основной метод экземпляра app класса MainApp
