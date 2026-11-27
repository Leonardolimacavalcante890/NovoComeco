#FUNÇÕES -> são criadas por nós quando desenvolvemos grandes estruturas, 
#pórem para reescrever seria trabalhoso

lista_precos = [10000, 5000, 2500, 1000, 500, 250]

#EXEMPLO COM IMPOSTOS

#Aliquota1 -> IRPJ = 0.15
#Aliquota2 -> CSLL = 0.09
#Aliquota3 -> PIS = 0.0065
#Aliquota4 -> COFINS = 0.03
#Aliquota5 -> ICMS = 0.17
#Aliquota6 -> IRPJ = 0.15

def calculo_imposto_total(precos):
    
    if precos <= 2000:
        imposto_irpj = 0.15 * precos
    else:
        imposto_irpj = 0.30 * precos    
    imposto_csll = 0.09 * precos
    imposto_pis = 0.0065 * precos
    imposto_cofins = 0.03 * precos
    imposto_icms = 0.17 * precos
        
    imposto_total = imposto_cofins + imposto_csll + imposto_icms + imposto_irpj + imposto_pis
    print(f"Imposto total sobre o produto R${precos}, sendo o imposto embutido: {imposto_total}")