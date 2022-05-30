from utils.usercheck import user_check
from utils.category import Category
from utils.goods import Goods

"""
Проверка логина и пароля пользователя
"""
user_check()

"""
Выбор категории товара
"""
Category.choose_category()





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
