from fastapi import FastAPI
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
