#INPUTS
# Ele existe para pedir uma informação ao usuário, ou seja, haver uma interação. Pode ser por POP-UP, arquivos e entre outros

input("Escreva seu email: ")

#Para poder armazenar uma dado feito pelo outro colega (Do outro lado), 
#então é preciso armazena-lá em uma VARIÁVEL

email = input("Email: ")
nome = input("Escreva seu primeiro nome: ")
idade = int(input("Quantos anos você tem? ")) # o INT transforma o valor em número, caso seja quebrado seria FLOAT
pos_nome = nome.find(" ")
pri_nome = nome[:pos_nome]
Adulto = idade - 18
print(email, nome)
print(f"Você já é velho há {Adulto} anos")

#Quando eles perguntam se o EMAIL está correto ou que foi enviado um link de confirmação, eles fazem assim:

print(f"{pri_nome}, verifique seu email: {email} no qual enviamos um link de confirmação")

#---------------------------------------------------------------------------------------
#LISTAS
# As listas tem NOME(VARIAVEL), dentro dos [] tem os items

#As listas de vendas no py normalmente são como:
vendas = [100, 80, 90, 70, 60, 40]

total_vendas = sum(vendas) #Assim como no Excel, SUM é somar
print(total_vendas)

#-------------------------------------------------------------------------
#TAMANHO DA LISTA
tamanho_vendas = len(vendas)
print(tamanho_vendas)

#-------------------------------------------------------------------------
#MAX e MIN
print(max(vendas))
print(min(vendas))

#-------------------------------------------------------------------------
#PEGAR POSIÇÃO
print(vendas[0]) #Vai pegar o 1° indice da lista
print(1,2) #Vai pegar o 2° e 3° item da lista

lista_de_produtos =["iphone","airpod","ipad","mackboook"]

produto_procurado = input("Pesquise pelo nome do produto: ").lower()
#minus_procurado = produto_procurado.lower()

print("iphone" in lista_de_produtos) # O IN é usado para saber se este produto está na LISTA
print(produto_procurado in lista_de_produtos) # dependendo do que ele escrever pode ser false ou true
print("Esse método seria para deixar todas as letras minusculas e conseguir decifrar o que é dito", produto_procurado, "min_procurado")

#------------------------------------------------------------------------
#ADICIONAR ITEM
lista_de_produtos.append("Apple Watch")
print(lista_de_produtos)

#-------------------------------------------------------------------------
#REMOVER UM ITEM
lista_de_produtos.remove("Apple Watch") #Aqui é preciso escrever para remover
print(lista_de_produtos)

lista_de_produtos.pop(-1)# Irá remover a última posição da lista
print(lista_de_produtos)

#-------------------------------------------------------------------------
#EDITAR UM ITEM
precos = [1000, 4000, 20000]
precos[0] = 5000 # Assim que edita uma lista, apenas selecionado a coluna que você quer editar
precos[1] = precos[1] * 1.5 #Caso você queira que o valor seja acrescentado +50% (porcentagem)
print(precos)
#-------------------------------------------------------------------------
#CONTAR QUANTAS VEZES UM ITEM APARECE NA LISTA
lista_de_produtos = ["iphone","airpod","ipad","mackboook""iphone","airpod","ipad","mackboook""iphone","airpod","ipad","mackboook"]
lista_precos = [1000, 4000, 20000, 1000, 4000, 20000, 1000, 4000, 20000, 1000, 4000, 20000]
print(lista_de_produtos.count("iphone")) #O COUNT conta quantas vezes tem aquele item na lista

#-------------------------------------------------------------------------
#ORDENAR LISTA - Seja em em ordem dos números ou de texto
lista_de_produtos.sort() #Irá ordenar em forma crescente
lista_precos.sort()
print(lista_de_produtos)
print(lista_precos)

lista_de_produtos.sort(reverse = True) #Serve para ordenar em forma decrescente, ou seja, se reverse é true, continue
lista_precos.sort()

print(lista_de_produtos)
print(lista_precos)