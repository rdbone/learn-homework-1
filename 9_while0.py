"""

Домашнее задание №1

   *Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    пока не встретится имя "Валера". Когда найдете, напишите "Валера нашелся". Подсказка: используйте метод list.pop()

   *Перепишите предыдуший пример в виде функции find_person(name), которая ищет имя в списке
   
"""
def find_person(name):
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    last_name = ""
    while last_name != name:
        if len(names) > 0:
            last_name = names.pop()
        else:
            print('Такого имени нет в списке') 
            break
    if last_name == name:
        print(f'{name} нашелся')
    print(f'Оставшиеся имена: {names}')

if __name__ == '__main__':
    find_name = input('Введите имя, которое ищем: ')
    find_person(find_name)