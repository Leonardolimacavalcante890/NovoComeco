#FOR - LOOP E ESTRUTURAS DE REPETIÇÃO
lista_vendas = [1000,500,250,2700,6000,4000]
meta = 1200
bonus = 0.1

# FOR 2 GRANDES ESTRUTURAS A SEREM USADAS
#1° FORMA DE ESTRUTURA DO FOR (menos usada na prática)
for i in range(10):
    print("Fique mais inteligente")

#2° FORMA DE ESTRUTURA DO FOR (mais utlizada ma prática)
for venda in lista_vendas: #Você pode colocar qualquer nome, seja ITEM, VENDA e assim por diante
    #Tudo o que estiver INDENTAÇÃO (com tab) e DENTRO do FOR irá se repetir
 #   print(venda) #Retornará todos os itens da Lista
    if venda >= meta:
        bonificacao = venda * bonus
        print(f"PARABÉNS, você receberá uma bonificação de 10%. O valor é de R${bonificacao}")
    else:
        print(f"infelizmente você não alcançou a meta, faltou R${meta - venda}. Tente na próxima.")


