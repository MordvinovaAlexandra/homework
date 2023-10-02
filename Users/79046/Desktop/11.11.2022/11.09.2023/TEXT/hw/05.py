'''Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.'''
import re
with open('5text.txt','r', encoding = 'utf-8') as f1:
    text = f1.read()
    # print(text)
    counting = text.count('человек')
    print('Слово встречается:', counting)
    
    # word = 'человека'
    # count = 0
    # for line in f1:
    #         words = line.split()
    #         for i in words:
    #             if(i==word):
    #                 count=count+1
    # print('Слово', word, 'встречается', ':', count)