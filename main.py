from utils.goods import Goods
from utils.usercheck import user_check
from utils.category import Category

"""
Проверка логина и пароля пользователя
"""
user_check()

"""
Выбор категории товара
"""
#Category.choose_category()

selected_category = int(input('Выберете категорию: '))

"""
Вывод категории товаров
"""

if selected_category == 1:
    name_categ = Category.name_category = 'Техника для уборки'
    print(name_categ)
    with open('clean.txt', 'r', encoding='utf-8') as file:
        print(file.read())
elif selected_category == 2:
    name_categ = Category.name_category = 'Техника для кухни'
    print(name_categ)
    with open('kitchen.txt', 'r', encoding='utf-8') as file:
        print(file.read())
elif selected_category == 3:
    name_categ = Category.name_category = 'Крупная бытовая техника'
    print(name_categ)
    with open('appliances.txt', 'r', encoding='utf-8') as file:
        print(file.read())
elif selected_category == 4:
    name_categ = Category.name_category = 'Встраиваемая техника'
    print(name_categ)
    with open('built-in.txt', 'r', encoding='utf-8') as file:
        print(file.read())
else:
    print('Упс, такой категории не существует :(')

"""
Добавление товара в корзину
"""
selected_item = str(input('Выберете товар, который хотите приобрести: '))
print('В корзине находится товар: ' + selected_item)