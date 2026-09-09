from sqlalchemy import Column, Integer, String, Float
from database import Base

#TabelaGasto
class GastoModel(Base):
    __tablename__ = "Gastos"

    idGasto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipoPagamento = Column(String, nullable=False)  # Ex: Crédito, Débito, Pix
    tipoBanco = Column(String, nullable=False)      # Ex: Itaú, Nubank, Bradesco
    nomeGasto = Column(String, nullable=False)      # Ex: Compra do mês
    empresaGasto = Column(String, nullable=False)   # Ex: Supermercado X
    dataGasto = Column(Integer, nullable=False)     # Armazena o timestamp ou formato AAAAMMDD
    valor = Column(Float, nullable=False) 

#TabelaGanho
class GanhoModel(Base):
    __tablename__ = "Ganhos"

    idGanho = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipoRecebimento = Column(String, nullable=False)  # Ex: Pix, Salário, TED
    tipoBanco = Column(String, nullable=False)        # Ex: Itaú, Nubank, Bradesco
    empresaGanho = Column(String, nullable=False)     # Ex: Empresa X, Cliente Y
    dataRecebimento = Column(Integer, nullable=False)  # Armazena o timestamp ou formato AAAAMMDD
    valor = Column(Float, nullable=False)             