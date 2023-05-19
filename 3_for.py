"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def total_product_sold(product_sold):
    total_sold_count = 0
    for item in product_sold:
        total_sold_count += item
    return total_sold_count
    
    
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    models_sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    total_sold = 0
    for model in models_sold:
        total_model_sold = total_product_sold(model["items_sold"])
        total_sold += total_model_sold
        print(f'Общее количество продаж модели {model["product"]}: {total_model_sold}')
        print(f'Среднее количество продаж модели {model["product"]}: {round(total_model_sold/len(model["items_sold"]))}')

    print(f'\nОбщее количество продаж всех товаров: {total_sold}')
    print(f'Среднее количество продаж по разным моделям: {round(total_sold/len(models_sold))}')

   
    
if __name__ == "__main__":
    main()
