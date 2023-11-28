from infra.configs.connection import DBConnection
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes

class AtoresRepository:
    def select(self):
        with DBConnection() as db:
            data = db.session.\
            query(Atores).\
            join(Filmes, Atores.titulo_filme == Filmes.titulo).\
            with_entities(
                Atores.nome,
                Filmes.genero,
                Filmes.titulo
                ).\
            all()
            return data