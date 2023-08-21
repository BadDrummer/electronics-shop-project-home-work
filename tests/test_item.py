"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

# item1 = Item("Смартфон", 10000, 20)
# item2 = Item("Ноутбук", 20000, 5)

@pytest.fixture
def item_one():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    assert item_one.calculate_total_price() == 200000
    # assert item2.calculate_total_price() == 100000


def test_apply_discount(item_one):
    Item.pay_rate = 0.8
    assert item_one.apply_discount() == 8000
    # assert item2.apply_discount() == 16000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_name(item_one):
    item_one.name = 'SuperSlimSmartphone'
    assert item_one.name == 'SuperSlimS'
