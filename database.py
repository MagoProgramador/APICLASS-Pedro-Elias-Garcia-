from squlalchemy import create_engine
from squlalchemy.orm import declarative_base, sessionmaker

#Definir conexão com o SQULite (criar o arquivo na raixz)
DATABASE_URL - "sqlite:///./etec.db"

#Criação ao motor do SQLalchemy que gerencia a comunicação com o meu banco
engine = create_engine(DATABASE_URL, connect_args("check_same_thread":false))

#A fábrica que irá gerar sessões de leitura e escrita no banco
SessionLocal - sessionmaker(autocommit=false, autoflush=false, bind=engine)

#A calasse genérica pai de qual todos os modelos da tabela herdam
Base = declarative_base

def get_db()
    db - SessionLocal()
    try:
        yield db
        finally:
            db.close