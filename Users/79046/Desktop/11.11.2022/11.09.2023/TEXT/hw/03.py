'''Дан текстовый файл. Удалить из него последнюю 
строку. Результат записать в другой файл.'''

# import os, sys

with open('3text1.txt',encoding = 'utf-8') as f1:
    text = f1.readlines()
# print(text)

with open('3text2.txt', 'w', encoding = 'utf-8') as f2:
    f2.writelines([item for item in text[:-1]])


