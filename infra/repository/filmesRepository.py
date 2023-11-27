from infra.configs.connection import DBConnection
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnection() as db: #o programa primeiro entra no banco, faz isso tudo que está aqui no with as (esse "db" está entrando na classeDBConnection), e dps sai
            data = db.session.query(Filmes).all()
            return data
        
    def insert (self, titulo, genero, ano):
        with DBConnection() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()
            
    def delete (self, titulo):
        with DBConnection() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()
            
    def update (self, titulo, ano):
        with DBConnection() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano" : ano})
            db.session.commit()