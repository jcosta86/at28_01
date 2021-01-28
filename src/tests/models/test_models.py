import sys
sys.path.append('.')
from src.models.category import Category
from src.models.base_model import BaseModel


def test_category_model_instance():
    name = 'name'
    description = 'description'

    cat = Category(name, description)

    assert isinstance(cat, Category)
    assert isinstance(cat, BaseModel)
    
    assert cat.name == name
    assert cat.description == description
    
def test_name_is_not_none():
    try:
        category_test = Category(None, 'description')
        raise AssertionError('The exception was not raised.')
    except Exception as e:
        assert isinstance(e, TypeError)
        assert e.args == ('Name is not string',)
    
def test_name_is_a_string():
    try:
        category_test = Category(1.6, 'description')
        raise AssertionError('The exception was not raised.')
    except Exception as e:
        assert isinstance(e, TypeError)
        assert e.args == ('Name is not string',)
       
def test_empty_name():
    try:
        category_test = Category(''*5, 'description')
        raise AssertionError('The exception was not raised.')
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.args == ('Name can not be empty',)

        
def test_name_len():
    try:
        category_test = Category('Name'*101, 'description')
        raise AssertionError('The exception was not raised.')
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.args == ('Name can not more thank 100 characters',)
                
 
def test_description_is_a_string():
    try:
        category_test = Category('name', 1.6)
        raise AssertionError('The exception was not raised.')
    except Exception as e:
        assert isinstance(e, TypeError)
        assert e.args == ('Description must be a string',)

def test_description_len():
    try:
        category_test = Category('Name', 'description'*255)
        raise AssertionError('The exception was not raised.')
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.args == ('Name can not more than 255 characters',)
      