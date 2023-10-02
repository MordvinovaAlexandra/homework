'''Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется 
пользователем.'''

with open('6text.txt', 'r', encoding = 'utf-8') as f1:
    text=f1.read()
    text = text.replace('что', 'КОТ')
# print(text)
    with open('6text1.txt', 'w', encoding = 'utf-8') as f2:
        f2.write(text)
