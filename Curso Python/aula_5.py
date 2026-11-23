#FOR - LOOP E ESTRUTURAS DE REPETIÇÃO
nome = input("Qual é o seu nome? ")
lista_vendas = [int(input("Qual foi seu faturamento nesse mês? "))]
meta1 = 1200
meta2 = 2400
# FOR 2 GRANDES ESTRUTURAS A SEREM USADAS
#1° FORMA DE ESTRUTURA DO FOR (menos usada na prática)
#for i in range(10):
#    print("Fique mais inteligente")

#2° FORMA DE ESTRUTURA DO FOR (mais utlizada ma prática)
for venda in lista_vendas: #Você pode colocar qualquer nome, seja ITEM, VENDA e assim por diante
    #Tudo o que estiver INDENTAÇÃO (com tab) e DENTRO do FOR irá se repetir
 #   print(venda) #Retornará todos os itens da Lista
    if venda >= meta2:
        bonificacao = venda * 0.12
        print(f"PARABÉNS {nome}, você receberá uma bonificação de 10%. O valor é de R${bonificacao}")
    else:
        print(f"infelizmente você não alcançou a meta, faltou R${meta2 - venda}. Tente na próxima.")

#MEU TESTE

for venda in lista_vendas:
    if venda >= meta2:
        bonus = 0.2 * venda
        print(f"Você bateu a meta {nome}!! Você terá uma bonificação de 20% sobre as vendas, sendo R${bonus} de bônus!!")    
    elif venda >= meta1:
        bonus = 0.12 * venda
        print(f"Você bateu a 1° meta {nome}!! Você terá uma bonificação de 5% sobre suas vendas, sendo R${bonus} de bônus")
    else:
        print("Infelizmente você não bateu nenhuma das 2 metas, pois ficou faltando R$", meta1 - venda, "para alcançar a 1° meta. MELHORE!!")

#OUTRO TESTE
email = input("Escreva seu email: ").lower()
pos_arroba = email.find("@")

for mail in email:
    if pos_arroba >= 1:
        confirmacao = input(f"{nome}, confirme seu email: ")
        if confirmacao == email:
            print("Seus dados foram salvos")
        else:
            print("Email incorreto")
    elif pos_arroba <= -1 or email != confirmacao:
        print("Esse email não existe, pois você não inseriu o @")
        tentativa_2 = input("Escreva novamente seu email: ").find("@")
        if tentativa_2 >= 1:
            print(tentativa_2)
            print("Muito bem")
print("fim do sistema")



