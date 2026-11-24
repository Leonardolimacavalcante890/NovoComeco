#DICIONÁRIOS E ESTRUTURA DE DADOS
lista_produtos = ["iphone","airpod","ipad","mackboook"]
precos = [2000, 9000, 6000, 11000]# Teria de ordenar em ordem com os produtos
# O OBJETIVO DO DICIONÁRIO é ROTULAR, ou seja, 2000 é o VALOR DO AIRPOD, 6000 é o VALOR DO IPHONE

dic_produtosTeste = {"chave": valor, "chave2": valor2,} # Essa é a estrutura do Dicionário

#APLICANDO FICARIA

dic_produtos1 = {"airpod": 2000, "iphone": 6000, "ipad": 9000, "mackbook": 11000} #Ao invés de 2 listas, usasse o dic

#O VALOR do dicionário pode ser uma LISTA DE INFORMAÇÕES
dic_produtos2 = {"airpod": [2000, 0], "iphone": [6000, 256], "ipad": [9000, 128], "mackbook": [11000, 480]} #Ao invés de 2 listas, usasse o dic

lista_produtos[0]#Na LISTA normalmente chamamos o nome da lista e a posição

#PEGAR um elemento 
print(dic_produtos2["airpod"]) # irá passar o ROTULO que o AIRPOD tem

#EDITAR um elemento
dic_produtos2["iphone"] = dic_produtos2["iphone"] * 1.3
print(dic_produtos2)

#QUANTIDADE de itens
print(len(dic_produtos2))

#REMOVER um item
dic_produtos2.pop("airpod")
print(dic_produtos2)

#ADICIONAR um item / MESMA FORMA DE EDITAR UM ELEMENTO
dic_produtos["apple watch"] = 2500 #Aqui foi adicionado o item e o seu valor
print(dic_produtos2)

#UM DICIONÁRIO NÃO DEIXA QUE SEJA INSERIDO elementos DUPLICATOS, por isso foi ADICIONADO O APPLE WATCH, pois não havia 1
#Porém não seria o mesmo com o "iphone", pois ele já está na lista

#VERIFICAR se um ITEM existe no DIC
if "iphone" in dic_produtos2 or 9000 in dic_produtos2: # Neste exemplo mostra apenas a CHAVE, pois ele só busca a chave
    print("Existe o produto")
else:
    print("Não existe")
#VERIFICAR se um VALOR existe nos valores do DIC
if 900 in dic_produtos2.values(): #O .VALUES() pega os VALORES e transforma em uma LISTA
    print("Existe")
else:
    print("Não existe")

#EXERCÍCIO

nome_produto = input("Nome do produto: ")
preco_produto = int(input("Preço do produto: "))

#Cadastrar o novo produto (se o produto não existir)
#Caso o produto exista ele vai editar o produto
if nome_produto in dic_produtos2:
    dic_produtos2[nome_produto] = dic_produtos2[nome_produto], preco_produto
    print(dic_produtos2)
else:
    dic_produtos2[nome_produto] = preco_produto
#O programa tem que no final atualizar o preço de todos os produtos para os novos valores
#São 10% original
for chave in dic_produtos2:
    chave = dic_produtos2.values() * 0.1
    print(dic_produtos2)