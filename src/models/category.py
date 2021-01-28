import sys
sys.path.append('.')
from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from src.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self,name:str, description:str) -> None:
        self.name = name
        self.description =  description
        
    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name is not string')
        if not name.strip():
            raise ValueError('Name can not be empty')
        if len(name) > 100:
            raise ValueError('Name can not more thank 100 characters')
        return name
    
    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description must be a string')
        if len(description) > 255:
            raise ValueError('Name can not more than 255 characters')
        return description
