import txt
from dataclasses import dataclass

@dataclass
class Category():
    num_category: int   # Номер категории
    name_category: str  # Название категории
    list_of_goods: list # Список товаров категории

    """"
    Вывод категории товаров
    """

    def choose_category():
        selected_category = input('Выберете категорию: ')


        if selected_category == '1':
            name_category = "Техника для уборки"
            print(name_category)
        elif selected_category == '2':
            name_category = "Техника для кухни"
            print(name_category)
        elif selected_category == '3':
            name_category = "Крупная бытовая техника"
            print(name_category)
        elif selected_category == '4':
            name_category = "Встраиваемая техника"
            print(name_category)
        else:
            print('Упс, такой категории не существует :(')

        """
        Просмотр товаров из выбранной категории
        """
        #i = 1
        #category_items = {}
        with open('goods.txt', 'r', encoding='utf-8') as file:
            print(file.read())
            #for line in file:
                #a = line.split(",")
                #if line.split(",")[0] == selected_category:
                    #items_str = Goods(line.split(",")[1], line.split(",")[2], line.split(",")[3])
                    #category_items[i] = items_str.goodsName, items_str.goodsPrice, items_str.goodsRate
                    #print(i, 'Название товара: ', items_str.goodsName, ' ', 'Цена товара: ', items_str.goodsPrice, ' ', 'Рейтинг товара: ', items_str.goodsRate)
                    #i += 1

        """
        Выбор товара
        """
        item = input('Выберите товар из категории: ')
