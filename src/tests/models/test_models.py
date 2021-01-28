import sys
sys.path.append('.')
from src.models.category import Category

# class Category(BaseModel):
#     __tablename__ = 'category'
#     name = Column('name', String(length=100), nullable=False)
#     description = Column('description', String(length=255), nullable=True)

#     def __init__(self,name:str, description:str) -> None:
#         self.name = name
#         self.description =  description
        
#     @validates('name')
#     def validate_name(self, key, name):
#         if not isinstance(name, str):
#             raise TypeError('Name is not string')
#         if not name.strip():
#             raise ValueError('Name can not be empty')
#         if len(name) > 100:
#             raise ValueError('Name can not more thank 100 characters')
#         return name
    
#     @validates('description')
#     def validate_description(self, key, description):
#         if not isinstance(description, str):
#             raise TypeError('Description must be a string')
#         if len(description) > 255:
#             raise ValueError('Name can not more than 255 characters')


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