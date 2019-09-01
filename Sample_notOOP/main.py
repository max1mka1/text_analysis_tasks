import re

f = open("text.txt", "r", encoding="utf-8")  #, encoding="utf-8"
text = f.read()
splited_text = re.split(" ", text)

print(splited_text)

for element in splited_text:
    result = re.match("\+7[0-9]{10}", element)
    result2 = re.match("8[0-9]{10}", element)
    if result:
        print(result.group(0), "\n")
    elif result2:
        print(result2.group(0), "\n")