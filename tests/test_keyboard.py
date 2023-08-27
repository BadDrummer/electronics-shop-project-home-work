from src.keyboard import Keyboard, LangMixin
import pytest


@pytest.fixture
def keyboard_one():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(keyboard_one):
    assert str(keyboard_one) == "Dark Project KD87A"


def test_language(keyboard_one):
    assert keyboard_one.language == 'EN'


def test_change_lang(keyboard_one):
    keyboard_one.change_lang()
    assert keyboard_one.language == 'RU'
    keyboard_one.change_lang().change_lang()
    assert keyboard_one.language == 'RU'


def test_set_lang(keyboard_one):
    with pytest.raises(AttributeError):
        keyboard_one.language = 'CH'
