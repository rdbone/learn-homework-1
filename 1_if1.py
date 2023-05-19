"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def activity(age):
    if age < 6:
        return 'Детский сад'
    elif 6 <= age < 18:
        return 'Школа'
    elif 18 <= age < 25:
        return 'ВУЗ'
    else:
        return 'Работа'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = int(input('Пожалуйста, введите свой возраст: '))
    user_activity = activity(user_age)
    print(f'Ваш род занятий: {user_activity}')
    
if __name__ == "__main__":
    main()
