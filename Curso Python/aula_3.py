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

#TAMANHO DA LISTA
tamanho_vendas = len(vendas)
print(tamanho_vendas)

#MAX e MIN
print(max(vendas))
print(min(vendas))

#PEGAR POSIÇÃO
print(vendas[0]) #Vai pegar o 1° indice da lista
print(1,2) #Vai pegar o 2° e 3° item da lista