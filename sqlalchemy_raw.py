from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

#Configurações
engine = create_engine("postgresql://natalia:natipedro14@localhost:5432/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine) #sessão baseada nas conexões que estarão no bd
session = Session()

#Entidades
class Filmes(Base):
    __tablename__ = "filmes" #essa entidade se relaciona com a tabela filmes do banco de dados
    
    titulo = Column (String, primary_key=True)
    genero = Column (String, nullable=False)
    ano = Column (Integer, nullable=False)
    
    def __repr__(self): #jeito que vai ser printado (mto soft)
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"

#Insert
data_insert = Filmes(titulo="O assassino da serra elétrica", genero="Drama", ano=1996) #é um objeto da classe Filmes :o
session.add(data_insert)
session.commit() #manda pro banco de dados


#Delete
session.query(Filmes).filter(Filmes.titulo == "Matilda").delete()
session.commit

#Update
session.query(Filmes).filter(Filmes.genero == "Drama").update({"ano":2000})
session.commit()

#SQL
#Select
data = session.query(Filmes).all() #essa query pega todos os elementos do banco relacionados relacionados à entidade Filmes
print(data)
'''
print(data[1].titulo)
print(data[0].ano, data[1].ano)
'''

session.close()

'''
#Utilização do SQL puro (só tem o primeiro import)
conn = engine.connect()
query = text('SELECT * FROM filmes')
result = conn.execute(query)
for row in result:
    print(row)
    print(row.titulo)
'''
