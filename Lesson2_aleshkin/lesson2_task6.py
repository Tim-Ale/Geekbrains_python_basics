"""
* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[

(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.

Пример:

{

“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

def create_products_structure():
    products = []
    while True:
        name = input("Введите название товара (или 'стоп' для завершения): ")
        if name == "стоп":
            break
        price = float(input("Введите цену товара: "))
        quantity = int(input("Введите количество товара: "))
        unit = input("Введите единицу измерения товара: ")
        product = (len(products) + 1, {"название": name, "цена": price, "количество": quantity, "ед": unit})
        products.append(product)
    return products


def analyze_products(products):
    analytics = {}
    for product in products:
        for key, value in product[1].items():
            if key not in analytics:
                analytics[key] = []
            analytics[key].append(value)
    return analytics


products = create_products_structure()
analytics = analyze_products(products)
print(analytics)