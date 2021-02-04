from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base_model import BaseModel


class Session:
    def __init__(self):
        connector = 'mysql+pymysql'
        host = 'mysql09-farm15.uni5.net'
        user = 'topskills17'
        password = 'ButecoOlist21'
        dbname = 'topskills17'
        self.__conn_string = f'{connector}://{user}:{password}@{host}:3306/{dbname}'
        self.__engine = create_engine(self.__conn_string)
        BaseModel.metadata.bind = self.__engine
        BaseModel.metadata.create_all()

    def __enter__(self):
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, traceback):
        self.__session.close()
        self.__engine.dispose()
