from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
    def __init__(self) -> None:
        self.__connection_string = "postgresql://natalia:natipedro14@localhost:5432/cinema"
        self.__engine = self.__create_database_engine()
        self.session = None
        
    def __create_database_engine(self): #cria a conexão com o bd
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self): #isso daqui entra na classe e cria uma sessão -> está sendo usado no filmesRepository
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): #sai da classe
        self.session.close() 