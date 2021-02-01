import pytest

from src.models.base_model import BaseModel
from src.models.category import Category


@pytest.mark.parametrize('name,description', [('Nome', 'Melhor time'), ('Test', 'Descrição')])
def test_category_model_instance(name, description):
    cat = Category(name, description)

    assert isinstance(cat, Category)
    assert isinstance(cat, BaseModel)

    assert cat.name == name
    assert cat.description == description


@pytest.mark.parametrize('name,description', [(None, 'Melhor time'), (1.6, 'Descrição')])
def test_name_must_be_str(name, description):
    with pytest.raises(TypeError) as exc:
        Category(name, description)
        assert 'must be' in exc.value


@pytest.mark.parametrize('name,description', [('', 'Melhor time'), ('' * 5, 'Descrição')])
def test_empty_name(name, description):
    with pytest.raises(ValueError) as exc:
        Category(name, description)
        assert 'can\'t be empty.' in exc.value


@pytest.mark.parametrize('name,description', [('Name' * 100, 'Melhor time'), ('a' * 101, 'Descrição')])
def test_name_len_greater_than_100(name, description):
    with pytest.raises(ValueError) as exc:
        Category(name, description)
        assert 'can\'t be greater than' in exc.value


@pytest.mark.parametrize('name,description', [('Test', None), ('Test', 5)])
def test_description_must_be_a_string(name, description):
    with pytest.raises(TypeError) as exc:
        Category(name, description)
        assert 'must be' in exc.value


@pytest.mark.parametrize('name,description', [('Name', 'Test' * 300), ('Test', 'A' * 256)])
def test_description_len_greater_than_255(name, description):
    with pytest.raises(ValueError) as exc:
        Category('Name', 'description' * 255)
        assert 'can\'t be greater than' in exc.value
