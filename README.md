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
nomeGasto: "Auto completar."

Para _input_(Ganho): tipoGanho, empresaGanho, tipoBanco, servicosPrestados, dataRecebimento.

tipoGanho: PIX, Crédito, Débito, Boleto e Cédula/Dinheiro.

Nas duas: tipoBanco.
**TabelaTroca:**Estou pensando na ideia de criar uma tabela para realizar a troca de TipoMoeda das tabelas.
Ex: Tenho R$20,00 no débito, e já está cadastrado no programa, quero sacar, agora possuo R$20,00 em dinheiro, que também será cadastrado no app. Nesta contra-
dição ocasiona em um dado incorreto de R$40,00 na soma, o que poderá causar confusão nas finanças, logo, criar um método para cancelar um dado e atribuir outro
dado no lugar(sobrepor)


__Auto Completar:__ É quando usamos um dado já atribuído na tabela, e que podemos utilizá-lo dinamizar.
__Cédula/Dinheiro__: Um deles será escolhido, não os dois.
__Banco para dinheiro:__ Quando o cliente for escolher dinheiro, o banco será desativado, indo para tabela __avulso__.
