from src.controllers.base_controller import BaseController
from src.controllers.category_controller import CategoryController
from src.models.category import Category
import pytest


@pytest.fixture
def create_instance():
    controller = CategoryController()
    return controller


def test_team_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CategoryController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)


def test_create_category(create_instance):
    name = 'NameCat'
    description = 'DescCat'
    cat = Category(name, description)

    result = create_instance.create(cat)

    assert result.id_ is not None
    assert result.name == name
    assert result.description == description

    create_instance.delete(result)


def test_update_category(create_instance):
    name = 'NameCat'
    description = 'DescCat'
    cat = Category(name, description)
    created = create_instance.create(cat)

    created.name = 'NameCat 2'
    created.description = 'DescCat 2'
    result = create_instance.update(created)

    assert result.id_ is not None
    assert result.name == 'NameCat 2'
    assert result.description == 'DescCat 2'

    create_instance.delete(result)


def test_delete_category(create_instance):
    name = 'NameCat'
    description = 'DescCat'
    cat = Category(name, description)
    created = create_instance.create(cat)

    create_instance.delete(created)

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(created.id_)
        assert exc.value == 'Object not found.'


def test_read_by_id_should_return_category(create_instance):
    name = 'NameCat'
    description = 'DescCat'
    cat = Category(name, description)
    created = create_instance.create(cat)

    result = create_instance.read_by_id(created.id_)

    assert isinstance(result, Category)
    assert result.name == name
    assert result.description == description

    create_instance.delete(created)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = CategoryController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(712893794895247)
    assert str(exc.value) == 'Object not found.'
