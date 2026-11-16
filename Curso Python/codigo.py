print("Hello, World!")
print("Meu nome é Leo")
print("Eu tenho 19 anos")

#Tipos de váriaveis

faturamento = 2500 # váriavel do tipo inteiro / int
custo = 1500.50 # variavel do tipo float / ponto flutuante
print("Tenho uma empresa com um faturamento de ", faturamento)
novas_vendas = 100
faturamento = faturamento + novas_vendas # A variável é chamada de váriavel pois ela pode mudar, sendo assim, ela assumi um novo valor.
imposto = faturamento * 0.10 #O imposto é embutido sobre o faturamento, logo é preciso coloca-ló antes do lucro, (lê de cima para baixo)

lucro = faturamento - custo - imposto #Colocar as váriantes de fazer o print, pois ele lê de cima para baixo.
margem_lucro = faturamento / custo
print("Tenho uma empresa com um faturamento e +1 venda dando: ", faturamento)
print("Também tenho um custo de", custo) 
print("Portanto, meu lucro líquido é de", lucro)
print("Já a margem líquida é", margem_lucro)
print("Arredondando ficaria:", round(margem_lucro, 2)) #Toda função do Python está em conjunto com parentêses  
#round é arredondar (número é a casa decimal)

mensagem = "O faturamento da loja foi de tanto"
email = "emailqualquer@gmail.com" #Tipo String -> Texto

teve_lucro = True # váriavel tipo boolean -> verdadeiro ou falso

#mod -> % resto da divisão (MMC, só que o resto, ou seja, o que não dá para fatorar é o RESTO)
print(10 % 3) # util quando for fazer conta de meses

#EXEMPLO
tempo_contrato = 170
tempo_anos = int(170 / 12)
print("Tempo em anos:", tempo_anos)

tempo_meses = tempo_contrato % 12
print("O tempo é", tempo_anos,"anos e", tempo_meses,"meses.")