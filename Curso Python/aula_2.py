email = "MEUEMAILegrandeeonardo@gmail.com"

faturamento = 10000
custo = 7700
lucro = faturamento - custo

print("O lucro da emrpresa foi de", lucro)
print("Faturamento da empresa: 1000, Custo: 700, Lucro: 300") #Esse é um exemplo quando o valor
#a variável é uma string, logo não é alterado o valor.

print("Faturamento da empresa: {}, Custo: {}, Lucro: {}" .format(faturamento, custo, lucro))
# Esse é um dos meios para que seja inserido valores dentro de uma string. (1° Forma)

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")
# A melhor forma, pois não é necessário fazer um certo raciocinio para saber onde está cada coisa

#---------------------------------------------------------------------

# BUSCAR INFORMAÇOES DE ACORDO COM OQ É INSERIDO NO TEXTO

#MAIUSCULA
email = "MEUEMAILeonardo@gmail.com".upper()
print(email)

#minuscula
email = "MEUEMAILeonardo@gmail.com".lower()
print(email)

#----------------------------------------------------------------------

#ENCONTRAR UM ELEMENTO DENTRO DE UM TEXTO ESPECÍFICO

#Exemplo: Encontrar o "@"
print(email.find("@")) #Ele irá dizer onde, em que posição está o "@", neste exemplo estaria na 
#posição 16 -> Bom para fazer processo de validação de emails

email_2 = "leonardosemarrobagmail.com"
print(email_2.find("@")) # Neste exemplo, como o email não tem @, então ele retornar o valor -1
#pois ele não encontrou

#---------------------------------------------------------------------

#Tamanho do texto (lentgh)
print(len(email)) #Ele ira contar o número de caracteres

#---------------------------------------------------------------------
#Pegar um caracter
print(email[1]) # Quiser selecionar algo, é feito com [] -> colocar a posição do elemento que deseja
#exemplo, número: 1, 3, 10 e assim por diante

# print(email[25]) #Retornara um erro

print(email[-1]) # Irá pegar de trás para frente, sendo então o M de .com

#Pegar um pedaço de texto
print(email_2[8:17]) # irá pegar da posição 8 para frente, ou seja SEMARROBA
#INTERVALO

print(email_2[:8]) #Começa do 0 ao 8, retornando LEONARDO

#----------------------------------------------------------------------

#SUBSTITUIÇÃO DE TEXTO

novo_email = email.replace("meuemail", "890") #A função REPLACE é divida da seguinte forma: 
#o que você quer tirar , o que você quer colocar (COLOCAR EM LETRA MAISUCULA OU MINUSCULA FAZ DIFERENÇA)
print(novo_email)

#----------------------------------------------------------------------

#Lidar com nomes
nome = "lEO lima"

print(nome.capitalize()) #Deixa a 1° letra maiuscula
print(nome.title()) #Deixa a 1° letra de cada palavra maiscula

#-----------------------------------------------------------------------

#TAREFA

# Atividade 1: pegar o servidor do email
posicao_arroba = email.find("@") + 1 # O +1 seria se eu não queresse o @ na busca do servidos
servidor = email[posicao_arroba:]
print(servidor)

#Atividade 2: Pegar o 1° nome

posicao_nome = nome.find(" ") 
pri_nome = nome[:posicao_nome]
print(pri_nome)
#Pegar o sobrenome 

sobrenome = nome[posicao_nome + 1:] 
print(sobrenome)

#------------------------------------------------------------------------

#CASOS ESPECIAIS
margem_lucro = lucro / faturamento

print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo}, Lucro: R${lucro} e a margem: {margem_lucro:.0%}") # Os (:) são colocados quando você quer formatar com algo, como %
                                #O F é utilizado para acrescentar essas 2 casas decimais      #O (.número) indica quantas casas decimais você quer até (%)
# if(email.find("@") = -1) return("Esse email está incorreto") else("Está tudo certinho")

