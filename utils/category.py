"""
Модуль для работы с категориями товаров
"""

class Category:
    """Тип данных Категория"""
    def __init__(self, num_category: int, name_category: str):
        self.num_category = num_category     # Номер категории
        self.name_category = name_category   # Название категории

    @classmethod
    def choose_cat(cls):
        """Выбор категории для просмотра товаров"""
        print('Выберите категорию товаров: ')
        with open('goods.txt','r', encoding='utf-8') as file:
            list_of_goods = []

            for line in file:
                a = line.split(",")[0]
                if a not in list_of_goods:
                    list_of_goods.append(a)
            i = 1
            for line in list_of_goods:
                print(f'{i} - {line}')
                i += 1


    def set_category_name(self, name_category):
        """Установка категории"""
        self.name_category = name_category

    def get_category_name(self):
        return self.name_category