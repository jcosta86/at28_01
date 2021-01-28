import sys
sys.path.append('.')
from sqlalchemy import Column, String

from src.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self,name:str, description:str) -> None:
        self.name = name
        self.description =  description