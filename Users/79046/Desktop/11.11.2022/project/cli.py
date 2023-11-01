'''
python cli.py add <good_item> <category_name> --frequency --notify [ email | telegram | sms ]
python cli.py query <good_item> <category_name>
python cli.py remove <id>
python cli.py update <id> --frequency --notify [ email | telegram | sms ]
python cli.py list
python cli.py report --all --id <id> --format [ web | pdf | spreadsheet | json | stdout ]
'''

import argparse

category_choices = [
    'Транспорт', 
    'Недвижимость', 
    'Личные вещи', 
    'Электроника, техника', 
    'Дом и сад, мебель, бытовое', 
    'Текстиль', 
    'Животные', 
    'Услуги и предложения', 
    'Работа', 
    'Хобби, Отдых, Спорт', 
    'Оборудование', 
    'Сырье', 
    'Строительные товары и услуги', 
    'Продукты питания'
                    ]

argparser = argparse.ArgumentParser(prog="kupiprodai")
subparser = argparser.add_subparsers(title='query')

query_command = subparser.add_parser('query')
query_command.add_argument('item', type=str)
query_command.add_argument('category_name', type=str, choices=category_choices)
query_command.add_argument('--save', type=bool, default=False)

add_command = subparser.add_parser('add')
add_command.add_argument('good_item', type=str)
add_command.add_argument('category_name', type=str, choices=category_choices)
add_command.add_argument('--frequency', type=int, default=24)
