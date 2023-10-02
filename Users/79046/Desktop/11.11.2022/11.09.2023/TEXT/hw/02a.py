'''Дан текстовый файл. Необходимо создать новый файл 
и записать в него следующую статистику по исходному 
файлу:
■ Количество символов;
■ Количество строк;
■ Количество гласных букв;
■ Количество согласных букв;
■ Количество цифр.'''

# Открываем файл для чтения
with open('2text1.txt',encoding = 'utf-8') as f1:
    text = f1.read()
print(text)

# Подсчет количества символов
num_chars = len(text)

# Подсчет количества строк
num_lines = text.count('\n') + 1

# Подсчет количества гласных и согласных букв
vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
num_vowels = 0
num_consonants = 0
for char in text:
    if char.isalpha():
        if char.lower() in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

# # Подсчет количества цифр
num_digits = sum(c.isdigit() for c in text)

# # Открываем файл для записи статистики
with open('2text2.txt', 'w', encoding = 'utf-8') as f1:
    f1.write(f'Кол-во символов: {num_chars}\n')
    f1.write(f'Кол-во строк: {num_lines}\n')
    f1.write(f'Кол-во гласных: {num_vowels}\n')
    f1.write(f'Кол-во согласных: {num_consonants}\n')
    f1.write(f'Кол-во цифр: {num_digits}\n')
