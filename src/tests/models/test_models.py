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
    except Exception as e:
        assert isinstance(e, TypeError)
        
        
def test_name_is_a_string():
    try:
        category_test = Category(1.6, 'description')
    except Exception as e:
        assert isinstance(e, TypeError)
        
def test_empty_name():
    try:
        category_test = Category(''*5, 'description')
    except Exception as e:
        assert isinstance(e, ValueError)
        
def test_name_len():
    try:
        category_test = Category('Name'*101, 'description')
    except Exception as e:
        assert isinstance(e, ValueError)                
 
def test_description_is_a_string():
    try:
        category_test = Category('name', 1.6)
    except Exception as e:
        assert isinstance(e, TypeError)

def test_description_len():
    try:
        category_test = Category('Name', 'description'*255)
    except Exception as e:
        assert isinstance(e, ValueError)             