from busket import Basket

class User:
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password
        self.__basket = Basket()
"""
Проверка логина и пароля пользователя
"""

def user_check():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    if login != 'Papa' or password != '1':
        print("Такой пользователь не найден, используйте другие данные для входа в магазин.")
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
    else:
        print("Добро пожаловать в магазин!")