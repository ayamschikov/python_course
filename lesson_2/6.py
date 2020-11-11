# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:

# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:

# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products = []
products_count = int(input('enter count of products you want to add: '))
iterator = 0
while iterator < products_count:
    print(f'enter product info #{iterator + 1}')
    products.append(
            (
                iterator + 1,
                {
                    'название': input('название: '),
                    'цена': input('цена: '),
                    'количество': input('количество: '),
                    'ед': input('ед: ')
                }
            )
    )
    iterator += 1

products_info = {
        'название': set(),
        'цена': set(),
        'количество': set(),
        'ед': set()
        }

print('products_info: ')

for product in products:
    for key, value in product[1].items():
        products_info[key].add(value)

print(products_info)
