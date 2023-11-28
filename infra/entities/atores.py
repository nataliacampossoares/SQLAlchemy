from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Atores(Base):
    __tablename__ = "atores" 
    
    id = Column (Integer, primary_key=True)
    nome = Column (String, nullable=False)
    titulo_filme = Column (Integer, ForeignKey("filmes.titulo"))
    
    def __repr__(self): 
        return f"Ator [nome={self.nome}, titulo={self.titulo_filme}]"
