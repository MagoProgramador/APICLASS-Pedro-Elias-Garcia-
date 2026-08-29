# APICLASS-Pedro-Elias-Garcia-
Projeto da aula de API da ETEC, nela iremos desenvolver um site de finanças, com foco em administrar os gastos e ganhos. 
Será elaborado para um único indivíduo, e não um conjunto pessoas ou empresa.
**Objetivo:** O cliente ter um software ou site/app que poderá usar como planilha de orçamento, seja para atribuir gastos ou ganhos.

**Funcional:** 
Do que cliente precisa?
De um campo que possa atribuir um dado que seja ele numérico, afinal, é o preço. (POST, String)
De um campo para nomear o tipo de pagamento, como pix, crédito, débito e dinheiro.(POST, String, com uma tabela fixa para tais tipos)
De uma célula para citar o produto, o nome relacionado a compra.(POST, String)
Da data para cada compra efetivada.(POST, Date)
No final a junção dos valores.($gasto1 + $gasto2 = soma ou $ganho1 + $ganho2 = soma)

**O cliente pretende corrigir um valor, qual método?**

Ao lado campo que já foi dado "baixa" terá um botão chamado "Redefinir", nele que ocorrerá essa atualização(PUT)

**O cliente pretende desfazer/apagar um valor, qual método?**

Ao lado botão "Redefinir" terá outro botão escrito "Apagar", nele efetivará o delete do dado(DELETE)

**Quantas tabelas será necessário?**


Para _input_(Gasto): tipoGasto, nomeGasto, empresaGasto, dataGasto e pagamento.

tipoGasto: PIX, Crédito, Débito, Boleto e Cédula/Dinheiro.

Para __input__(Ganho): tipoGanho, empresaGanho, tipoBanco, servicosPrestados, dataRecebimento.

tipoGanho: PIX, Crédito, Débito, Boleto e Cédula/Dinheiro.

Nas duas: tipoBanco.
