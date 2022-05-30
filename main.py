from utils.usercheck import user_check
from utils.category import Category
from utils.goods import Goods

"""
Проверка логина и пароля пользователя
"""
user_check()

"""
Выборк категории товара
"""
Category.choose_category()

"""
Выбор товара из категории
"""

i = 1
items = {}
with open('goods.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a = line.split(",")
        if line.split(",")[0] == Category.:
            items_str = Goods(line.split(",")[1], line.split(",")[2], line.split(",")[3])
            items[i] = items_str.goodsName, items_str.goodsPrice, items_str.goodsRate
            print(i, 'Название товара: ', items_str.goodsName, ' ', 'Цена товара: ', items_str.goodsPrice, ' ', 'Рейтинг товара: ', items_str.goodsRate)
            i += 1

item = input('Выберите товар из категории: ')



#selected_category = int(input("Выберете категорию товаров: "))

#"""
#Вывод наименования категорий
#"""
#if selected_category == 1:
    #name_categ = Category(name_category = 'Техника для уборки')
    #print(name_categ.name_category)
#elif selected_category == 2:
   # name_categ = Category(name_category='Техника для кухни')
   # print(name_categ.name_category)
#elif selected_category == 3:
   # name_categ = Category(name_category = 'Крупная бытовая техника')
   # print(name_categ.name_category)
#elif selected_category == 4:
   # name_categ = Category(name_category = 'Встраиваемая техника')
   # print(name_categ.name_category)
#else:
   # print('Упс, такой категории не существует :(')
