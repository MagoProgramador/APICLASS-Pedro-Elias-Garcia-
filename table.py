from pydantic import AtribuirGasto, AtribuirGanho

#Denifição da Tabela de Gastos.
#OBS: Descobrir como implantar dados já estabelecidos no banco
class GastosSchema(AtribuirGasto):
    
    idGasto: int
    tipoPagamento: str
    tipoBanco: str
    nomeGasto: str
    empresaGasto: str 
    dataGasto: int
    valor: float

#Denifição da Tabela de Ganhos 
class GanhosSchema(AtribuirGanho):
    
    idGanho: int
    tipoRecebimento: str
    tipoBanco: str
    empresaGanho: str 
    dataRecebimento: int
    valor: float

    #Permitir que o Pydantic leia diretamente os objetos do meu banco de dados

    class Config:
        from_atributes = True