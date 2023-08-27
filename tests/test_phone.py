from src.phone import Phone
import pytest


@pytest.fixture
def phone_one():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone_one):
    assert repr(phone_one) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone_one):
    assert str(phone_one) == 'iPhone 14'


def test_number_of_sim(phone_one):
    phone_one.number_of_sim = 5
    assert phone_one.number_of_sim == 5


def test_number_of_sim_error(phone_one):
    with pytest.raises(ValueError):
        phone_one.number_of_sim = 0
