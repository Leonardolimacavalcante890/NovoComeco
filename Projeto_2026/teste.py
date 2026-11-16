email = "MEUEMAILeonardo@gmail.com"

faturamento = 1000
custo = 700
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

#Tamanho do texto (lentgh)
print(len(email)) #Ele ira contar o número de caracteres

#Pegar um caracter
print(email[1]) # Quiser selecionar algo, é feito com [] -> colocar a posição do elemento que deseja
#exemplo, número: 1, 3, 10 e assim por diante

print(email[25]) #Retornara um erro

print(email[-1]) # Irá pegar de trás para frente, sendo então o M de .com

#Pegar um pedaço de texto
print(email[:4]) # irá pegar da posição 4 para trás, ou seja MEUE
#INTERVALO

if(email.find("@") = -1)
return("Esse email está incorreto")
else("Está tudo certinho")