"""
Проверка логина и пароля пользователя

:param login: логин польз-ля
:param password: пароль польз-ля
"""

def user_check():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    if login != 'Papa' or password != '1':
        print("Такой пользователь не найден, используйте другие данные для входа в магазин.")
        breakpoint()
    else:
        print("Добро пожаловать в магазин!")