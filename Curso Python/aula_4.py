#CONDIÇÕES
#if condicao/comparacao:
    #Tudo que acontece se por acaso a condição for verdadeira 
    #VOCÊ pode TERMINAR AQUI ou
#else: 
    #Caso a 1° condição seja falsa, ele irá RETORNAR TUDO O QUE ESTA AQUI   

#----------------------------------------------------------------------
vendas = int(input("Qual é a sua quantia de vendas atualmente? "))
meta = 1600

#TIPOS DE COMPARADORES
# Maior que >
# Menor que <
# Maior ou igual >=
# Menor ou igual <=
# igual == Tem que ser extamente IGUAL
# Diferente !=
if vendas >= meta:
    diferenca = vendas - meta
    print(f"O vendedor irá ganhar bonificação pois alcançou a meta, sendo: {int(diferenca)} a diferença")
    bonus = 0.1 * vendas
    print(f"O bonûs do vendedor será 10% de suas vendas {bonus}")
else:
    print("Ele não alcançou a meta, então não irá ter bônus")

print("Isso será sempre executado indiferente da condição, pois está sem TAB e 'fora da condição'")

#--------------------------------------------------------------------------------------------------
#É POSSÍVEL FAZER UMA CONDIÇÃO SOBRE OUTRA CONDIÇÃO
vendas = int(input("Qual é a sua quantia de vendas atualmente? "))
meta1 = 1500
meta2 = 2000

if vendas >= 2000:
    bonus = 0.2 * vendas
    print(f"Você bateu a meta!! Você terá uma bonificação de 20% sobre as vendas, sendo R${bonus} de bônus!!")
else:
    if vendas >= meta1: #ESSE IF E ELSE estão DENTRO de um ELSE
        bonus = 0.1 * vendas
        print(f"Você bateu a 1° meta!! Você terá uma bonificação de 10% sobre suas vendas, sendo R${bonus} de bônus")
    else:
        print("Infelizmente você não bateu nenhuma das 2 metas, pois ficou faltando R$", meta1 - vendas, "para alcançar a 1° meta")

#--------------------------------------------------------------------------------------------------
#OUTRA FORMA DE FAZER ESSE MÉTODO (ELIF)
if vendas >= 2000:
    bonus = 0.2 * vendas
    print(f"Você bateu a meta!! Você terá uma bonificação de 20% sobre as vendas, sendo R${bonus} de bônus!!")
elif vendas >= meta1: #ELE É TIPO UM 2° IF para caso 1° não seja validado
    bonus = 0.05 * vendas
    print(f"Você bateu a 1° meta!! Você terá uma bonificação de 5% sobre suas vendas, sendo R${bonus} de bônus")
else: #Continua com a mesma estrutura, finalizando com ELSE
    print("Infelizmente você não bateu nenhuma das 2 metas, pois ficou faltando R$", meta1 - vendas, "para alcançar a 1° meta. MELHORE!!")

#--------------------------------------------------------------------------------------------------
#CONTINUANDO E AUTOMATIZANDO AQUILO NO QUAL FIZEMOS NA LISTA
lista_produtos = ["iphone","airpod","ipad","mackboook"]
produto_proc = input("Escreva o item que você deseja: ").lower()

if produto_proc in lista_produtos: #O IF é utilizado para condições, ou seja: TRUE OU FALSE
    print("Este produto está no estoque")
else: #Fiz +1 condição para que caso a pessoa errasse, teria uma 2° chance
    print("Esse produto não está no estoque. ")
    print(f"Temos os seguintes produtos: {lista_produtos}")
    produto_proc2 = input("Escreva algum item que está nessa lista: ").lower()
    if produto_proc2 in lista_produtos:
        print(f"{produto_proc2} está em estoque.")
    else:
        print("Você é burro?")

#elif produto_proc in lista_produtos == False:
  #  print("Esse produto não está no estoque. ")
  #  print(f"Temos os seguintes produtos: {lista_produtos}")
 #   produto_proc2 = input("Escreva algum item que está nessa lista: ").lower()
   # print(f"{produto_proc2} está em estoque.")
#else:
  #  print("Você é burro?")

#--------------------------------------------------------------------------------------------------
#AS CONDIÇÕES PODEM SER MAIS DE UMA
venda_empresa = int(input("Fala meu gestor, qual foi o faturamento das vendas esse mês: "))
meta_empresa = 15000

#OUTROS TIPOS DE CONDIÇÕES
# AND - Adiciona +1 condição (AS 2 devem ser verdadeiras)
# OR - Entre uma ou outra (1 das 2 devem ser verdadeiras)

if vendas >= 2000 and venda_empresa >= meta_empresa:
    bonus = 0.2 * vendas
    print(f"Você bateu a meta!! Você terá uma bonificação de 20% sobre as vendas, sendo R${bonus} de bônus!!")
elif vendas >= meta1 and venda_empresa >= meta_empresa: #ELE É TIPO UM 2° IF para caso 1° não seja validado
    bonus = 0.05 * vendas
    print(f"Você bateu a 1° meta!! Você terá uma bonificação de 5% sobre suas vendas, sendo R${bonus} de bônus")
else: #Continua com a mesma estrutura, finalizando com ELSE
    print("Infelizmente você não bateu nenhuma das 2 metas, pois ficou faltando R$", meta1 - vendas, "para alcançar a 1° meta. MELHORE!!")
