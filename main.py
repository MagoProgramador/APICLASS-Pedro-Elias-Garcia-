from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

#ATT 1
app = FastAPI(
    title="API Financeira",
    description="API para controle de gastos e ganhos de um usuário.",
    version="1.0.0"
)
# =========================
# Simulação de extrato
# =========================
gastos = [
    {
        "id": 1,
        "tipoGasto": "Alimentação",
        "nomeGasto": "Mercado",
        "empresaGasto": "Carrefour",
        "dataGasto": "2026-08-25",
        "pagamento": "PIX",
        "valor": 150.50
    },
    {
        "id": 2,
        "tipoGasto": "Transporte",
        "nomeGasto": "Combustível",
        "empresaGasto": "Posto Shell",
        "dataGasto": "2026-08-26",
        "pagamento": "Crédito",
        "valor": 200.00
    },
    {
        "id": 3,
        "tipoGasto": "Lazer",
        "nomeGasto": "Cinema",
        "empresaGasto": "Cinemark",
        "dataGasto": "2026-08-27",
        "pagamento": "Débito",
        "valor": 45.00
    },
    {
        "id": 4,
        "tipoGasto": "Moradia",
        "nomeGasto": "Conta de luz",
        "empresaGasto": "Enel",
        "dataGasto": "2026-08-28",
        "pagamento": "Boleto",
        "valor": 120.75
    },
    {
        "id": 5,
        "tipoGasto": "Alimentação",
        "nomeGasto": "Padaria",
        "empresaGasto": "Padaria Central",
        "dataGasto": "2026-08-29",
        "pagamento": "Cédula/Dinheiro",
        "valor": 25.00
    }
]
ganhos = [
    {
        "id": 1,
        "tipoGanho": "Salário",
        "empresaGanho": "Empresa XYZ",
        "tipoBanco": "Nubank",
        "servicosPrestados": "Salário mensal",
        "dataRecebimento": "2026-08-05",
        "valor": 2500.00
    },
    {
        "id": 2,
        "tipoGanho": "Freelance",
        "empresaGanho": "Cliente A",
        "tipoBanco": "Inter",
        "servicosPrestados": "Desenvolvimento de site",
        "dataRecebimento": "2026-08-10",
        "valor": 800.00
    },
    {
        "id": 3,
        "tipoGanho": "Freelance",
        "empresaGanho": "Cliente B",
        "tipoBanco": "Itaú",
        "servicosPrestados": "Design gráfico",
        "dataRecebimento": "2026-08-15",
        "valor": 450.00
    },
    {
        "id": 4,
        "tipoGanho": "Venda",
        "empresaGanho": "Cliente C",
        "tipoBanco": "Nubank",
        "servicosPrestados": "Venda de produto",
        "dataRecebimento": "2026-08-20",
        "valor": 300.00
    },
    {
        "id": 5,
        "tipoGanho": "Freelance",
        "empresaGanho": "Cliente D",
        "tipoBanco": "Banco do Brasil",
        "servicosPrestados": "Manutenção de computador",
        "dataRecebimento": "2026-08-25",
        "valor": 250.00
    }
]
# =========================
# ROTA RAIZ
# GET /
# =========================
@app.get("/")
def raiz():
    return {
        "status": "online",
        "mensagem": "API Financeira funcionando!"
    }
# =========================
# ROTA DE GASTOS
# GET /gastos
# =========================

@app.get("/gastos")
def listar_gastos():
    return gastos
# =========================
# ROTA DE GANHOS
# GET /ganhos
# =========================
@app.get("/ganhos")
def listar_ganhos():
    return ganhos

#ATT 2


# Cria as tabelas no arquivo financas.db se elas não existirem
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Controle Financeiro")


# ==========================================
# CRUD - GASTOS
# ==========================================

@app.post("/gastos/", response_model=schemas.GastosSchema, status_code=status.HTTP_201_CREATED)
def criar_gasto(gasto: schemas.AtribuirGasto, db: Session = Depends(get_db)):
    db_gasto = models.GastoModel(**gasto.model_dump())
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

@app.get("/gastos/", response_model=List[schemas.GastosSchema])
def listar_gastos(db: Session = Depends(get_db)):
    return db.query(models.GastoModel).all()

@app.get("/gastos/{id_gasto}", response_model=schemas.GastosSchema)
def obter_gasto(id_gasto: int, db: Session = Depends(get_db)):
    db_gasto = db.query(models.GastoModel).filter(models.GastoModel.idGasto == id_gasto).first()
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    return db_gasto

@app.put("/gastos/{id_gasto}", response_model=schemas.GastosSchema)
def atualizar_gasto(id_gasto: int, gasto_atualizado: schemas.AtribuirGasto, db: Session = Depends(get_db)):
    db_gasto = db.query(models.GastoModel).filter(models.GastoModel.idGasto == id_gasto).first()
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    
    for key, value in gasto_atualizado.model_dump().items():
        setattr(db_gasto, key, value)
        
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

@app.delete("/gastos/{id_gasto}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_gasto(id_gasto: int, db: Session = Depends(get_db)):
    db_gasto = db.query(models.GastoModel).filter(models.GastoModel.idGasto == id_gasto).first()
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    db.delete(db_gasto)
    db.commit()
    return None


# ==========================================
# CRUD - GANHOS
# ==========================================

@app.post("/ganhos/", response_model=schemas.GanhosSchema, status_code=status.HTTP_201_CREATED)
def criar_ganho(ganho: schemas.AtribuirGanho, db: Session = Depends(get_db)):
    db_ganho = models.GanhoModel(**ganho.model_dump())
    db.add(db_ganho)
    db.commit()
    db.refresh(db_ganho)
    return db_ganho

@app.get("/ganhos/", response_model=List[schemas.GanhosSchema])
def listar_ganhos(db: Session = Depends(get_db)):
    return db.query(models.GanhoModel).all()

@app.get("/ganhos/{id_ganho}", response_model=schemas.GanhosSchema)
def obter_ganho(id_ganho: int, db: Session = Depends(get_db)):
    db_ganho = db.query(models.GanhoModel).filter(models.GanhoModel.idGanho == id_ganho).first()
    if not db_ganho:
        raise HTTPException(status_code=404, detail="Ganho não encontrado")
    return db_ganho

@app.put("/ganhos/{id_ganho}", response_model=schemas.GanhosSchema)
def atualizar_ganho(id_ganho: int, ganho_atualizado: schemas.AtribuirGanho, db: Session = Depends(get_db)):
    db_ganho = db.query(models.GanhoModel).filter(models.GanhoModel.idGanho == id_ganho).first()
    if not db_ganho:
        raise HTTPException(status_code=404, detail="Ganho não encontrado")
    
    for key, value in ganho_atualizado.model_dump().items():
        setattr(db_ganho, key, value)
        
    db.commit()
    db.refresh(db_ganho)
    return db_ganho

@app.delete("/ganhos/{id_ganho}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_ganho(id_ganho: int, db: Session = Depends(get_db)):
    db_ganho = db.query(models.GanhoModel).filter(models.GanhoModel.idGanho == id_ganho).first()
    if not db_ganho:
        raise HTTPException(status_code=404, detail="Ganho não encontrado")
    db.delete(db_ganho)
    db.commit()
    return None
#Honestamente não entendo meu código