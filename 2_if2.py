"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def str_compare(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3
    else:
        return 'No result of comparison'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(str_compare(0, 'привет')) #вернет 0
    print(str_compare('привет', True)) #вернет 0
    print(str_compare('привет', 'привет')) #вернет 1
    print(str_compare('приветик', 'привет')) #вернет 2
    print(str_compare('приветик', 'learn')) #вернет 2
    print(str_compare('hi', 'learn')) #вернет 3
    
if __name__ == "__main__":
    main()
