import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = 'File item.csv is damaged or empty'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("При сложении оъекта должен быть типа Item или его потомками")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, path=CSV_PATH):
        """instantiation of class Item with data from items.csv file"""
        cls.all = []
        try:
            with (open(path) as csvfile):
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
                    if len((name, price, quantity)) != 3:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print('File item.csv not found')
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(num_str) -> int:
        """returns int from str number"""
        return int(float(num_str))
