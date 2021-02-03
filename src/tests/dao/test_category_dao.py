
import pytest
from sqlalchemy.orm.exc import UnmappedInstanceError

from src.dao.base_dao import BaseDao
from src.dao.category_dao import CategoryDao
from src.models.category import Category


class TestCategoryDao:
    @pytest.fixture
    def create_instance(self):
        return CategoryDao()


    def test_instance(self, create_instance):
        assert isinstance(create_instance, CategoryDao)
        assert isinstance(create_instance, BaseDao)

    def test_save(self, create_instance):
        category = Category('nome', 'desc')
        category_saved = create_instance.save(category)

        assert category_saved.id_ is not None
        create_instance.delete(category_saved)

    def test_not_save(self, create_instance):
        with pytest.raises(UnmappedInstanceError):
            create_instance.save('category')

    def test_read_by_id(self, create_instance):
        category = Category('nome', 'desc')
        category_saved = create_instance.save(category)
        category_read = create_instance.read_by_id(category_saved.id_)

        assert isinstance(category_read, Category)
        CategoryDao().delete(category_read)

    def test_not_read_by_id(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.read_by_id('category_saved.id_')

    def test_read_all(self, create_instance):
        category_read = create_instance.read_all()
        assert isinstance(category_read, list)

    def test_delete(self, create_instance):
        category = Category('nome', 'desc')
        category_saved = create_instance.save(category)
        category_read = create_instance.read_by_id(category_saved.id_)
        create_instance.delete(category_read)
        category_read = create_instance.read_by_id(category_saved.id_)

        assert category_read is None

    def test_not_delete(self, create_instance):
        with pytest.raises(UnmappedInstanceError):
            create_instance.delete('category_read')
