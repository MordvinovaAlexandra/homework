'''Дан текстовый файл. Найти длину самой длинной строки.'''
with open('4text.txt','r', encoding = 'utf-8') as f1:
    max_line = max((line.strip() for line in f1))
print(max_line)

