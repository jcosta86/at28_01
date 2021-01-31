import sys

sys.path.append('.')
from src.models.category import Category
from src.models.base_model import BaseModel
import pytest


def test_category_model_instance():
    name = 'name'
    description = 'description'

    cat = Category(name, description)

    assert isinstance(cat, Category)
    assert isinstance(cat, BaseModel)

    assert cat.name == name
    assert cat.description == description


def test_name_is_not_none():
    with pytest.raises(TypeError):
        category_test = Category(None, 'Melhor time do Brasil')


def test_name_is_a_string():
    with pytest.raises(TypeError):
        category_test = Category(1.6, 'description')


def test_empty_name():
    with pytest.raises(ValueError):
        category_test = Category('' * 5, 'description')


def test_name_len():
    with pytest.raises(ValueError):
        category_test = Category('Name' * 101, 'description')


def test_description_is_a_string():
    with pytest.raises(TypeError):
        category_test = Category('name', 1.6)


def test_description_len():
    with pytest.raises(ValueError):
        category_test = Category('Name', 'description' * 255)
        raise AssertionError('The exception was not raised.')

