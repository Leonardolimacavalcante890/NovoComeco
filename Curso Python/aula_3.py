#INPUTS
# Ele existe para pedir uma informação ao usuário, ou seja, haver uma interação. Pode ser por POP-UP, arquivos e entre outros

email = input("Escreva seu email: ")

#Para poder armazenar uma dado feito pelo outro colega (Do outro lado), 
#então é preciso armazena-lá em uma VARIÁVEL

nome = input("Escreva seu primeiro nome: ")
idade = int(input("Quantos anos você tem? ")) # o INT transforma o valor em número, caso seja quebrado seria FLOAT
pos_nome = nome.find(" ")
pri_nome = nome[:pos_nome] #Realmente funcionaSa
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
print("Esse é o total de vendas", total_vendas)

#-------------------------------------------------------------------------
#TAMANHO DA LISTA
tamanho_vendas = len(vendas)
print("Isso é para saber quantos items tem na lista: ",tamanho_vendas)

#-------------------------------------------------------------------------
#MAX e MIN
print("Esse é o maior da lista de vendas: ", max(vendas))
print("Esse é o menor da lista de vendas: ", min(vendas))

#-------------------------------------------------------------------------
#PEGAR POSIÇÃO
print("É para saber qual item está na posição exigida: ", vendas[0]) #Vai pegar o 1° indice da lista
print("Pegando outras 2 posições: ", vendas[1], vendas[2]) #Vai pegar o 2° e 3° item da lista

lista_de_produtos =["iphone","airpod","ipad","mackboook"]

produto_procurado = input("Pesquise pelo nome do produto: ").lower()
#minus_procurado = produto_procurado.lower()

# print("iphone" in lista_de_produtos) # O IN é usado para saber se este produto está na LISTA
print(produto_procurado in lista_de_produtos) # dependendo do que ele escrever pode ser false ou true
print("Esse método seria para deixar todas as letras minusculas e conseguir decifrar o que é dito ", produto_procurado)

#------------------------------------------------------------------------
#ADICIONAR ITEM
print("Lista de produtos antes da adição: ", lista_de_produtos)
adicao_produtos = input("Qual item você gostaria de adicionar? ").lower()
lista_de_produtos.append(adicao_produtos)
print("Será adicionado a lista de produtos: ", adicao_produtos)
print("Essa é a nova lista de produtos: ", lista_de_produtos)

#-------------------------------------------------------------------------
#REMOVER UM ITEM
remove_produtos = input("O que você deseja excluir: ")
lista_de_produtos.remove(remove_produtos) #Aqui é preciso escrever para remover
print("Aqui irá remover o produto que antes foi acrescentado: ", lista_de_produtos)

lista_de_produtos.pop(-1)# Irá remover a última posição da lista
print("Aqui você escolhe qual posição você deseja tirar da lista: ",lista_de_produtos)

#-------------------------------------------------------------------------
#EDITAR UM ITEM
precos = [1000, 4000, 20000]
print("Esse são os preços antes de serem editados: ", precos)
precos[0] = 5000 # Assim que edita uma lista, apenas selecionado a coluna que você quer editar
precos[1] = precos[1] * 1.5 #Caso você queira que o valor seja acrescentado +50% (porcentagem)
print("Esse é valor após a alteração dos preços: ", precos)
#-------------------------------------------------------------------------
#CONTAR QUANTAS VEZES UM ITEM APARECE NA LISTA
lista_de_produtos = ["iphone","airpod","ipad","mackboook","iphone","airpod","ipad","mackboook","iphone","airpod","ipad","mackboook"]
lista_precos = [1000, 4000, 20000, 1000, 4000, 20000, 1000, 4000, 20000, 1000, 4000, 20000]
print("Retornará quantas vezes tem o item iphone: ", lista_de_produtos.count("iphone")) #O COUNT conta quantas vezes tem aquele item na lista
print("Retornará quantas vezes tem o número que deseja: ", lista_precos.count(1000))
#-------------------------------------------------------------------------
#ORDENAR LISTA - Seja em em ordem dos números ou de texto
lista_de_produtos.sort() #Irá ordenar em forma crescente
lista_precos.sort()
print("Ordenado em forma crescente: ", lista_de_produtos)
print("Ordenado em forma crescente: ", lista_precos)

lista_de_produtos.sort(reverse = True) #Serve para ordenar em forma decrescente, ou seja, se reverse é true, continue
lista_precos.sort(reverse = True)

print("Agora eles foram ordenados em forma decrescente: ", lista_de_produtos)
print("Agora eles foram ordenados em forma decrescente: ", lista_precos)