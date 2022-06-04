import re

from usercheck import user_check
from category import Category
from goods import Goods
from basket import Basket

"""
Проверка логина и пароля пользователя
"""
user_check()

total_basket = {}
j = 1

"""
Выбор категории товара
"""
Category.choose_cat()

choosen_cat = int(input('Выберите категорию: '))

categ_name = Category(0, '')
if choosen_cat == 1:
    categ_name.set_category_name('Встраиваемая техника')
elif choosen_cat == 2:
    categ_name.set_category_name('Крупная бытовая техника')
elif choosen_cat == 3:
    categ_name.set_category_name('Техника для уборки')
elif choosen_cat == 4:
    categ_name.set_category_name('Техника для кухни')
else:
    print('Указанной категории не существует')
    breakpoint()

print(categ_name.get_category_name())

"""
Вывод списка товаров категории
"""
i = 1
product_dict = {}  # создаем пустой словарь
with open("goods.txt", encoding="utf-8") as file:
    for line in file:
        if line.split(",")[0] == categ_name.get_category_name():
            product_srt = Goods(line.split(",")[1], line.split(",")[2], line.split(",")[3])
            product_dict[i] = product_srt.goodsName, product_srt.goodsPrice, product_srt.goodsRate
            print(i, 'Товар:', product_srt.goodsName, '; Цена товара: ', product_srt.goodsPrice, '; Рейтинг товара: ', product_srt.goodsRate)
            i += 1  # подсчет количества строк

"""
Добавление товара в корзину
"""
choosen_goods = int(input("Укажите номер товара, добавляемого в корзину: "))

"""
Проверка существования товара в ассортименте
"""

if choosen_goods not in product_dict:
    print('Такого товара нет в нашем ассортименте :(' )
    choosen_goods = int(input("Выберите другой товар из списка: "))
else:
    basket_1 = Basket(product_dict[choosen_goods])
    # basket_2 = re.sub("[(|'|)]", " ", str(basket_1.item_name))
    basket_2 = re.sub("[(|')]", "", str(basket_1.item_name))
    print('В корзину добавлен товар', basket_2)
    basket_3 = int(basket_2.rpartition(' ')[-1])
    total_basket[j] = basket_3

# re.su

# """
# Вывод инфо о корзине
# """
#
#  if choosen_goods in product_dict:


Basket.sum_basket(total_basket)


# """
# Вывод инфо о корзине
# """
#
#
# if
#
# print('В корзине находится товар под номером', choosen_goods, 'на сумму', product_srt.goodsPrice, 'руб.')