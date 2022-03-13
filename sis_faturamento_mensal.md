#Definindo os salários fixos
salario_fixo_vendedor = 1000.00
salario_fixo_gerente = 2000.00

#Definindo os funcionários para uma melhor manipulação
no_funcionario = ['Emily (vendedora)', 'Larissa (vendedora)', 'Rafael (vendedor)', 'Milena (vendedora)']
no_gerente = ['Jessica (gerente)']

#Criando lista de vendas efetuadas pelos vendedores
vendas_efetuadas = list()
for i in no_funcionario:
    # Capturando e tratando os valores digitados
      while True:
        try:
            venda = float(input(f'Digite as vendas mensais do(a) {i}: '))
            if venda < 0:
                print('\033[31m[31mValor INVÁLIDO! Digite apenas valores maiores ou iguais a "0":\033[m')
            break
        except:
            print('\033[31mValor INVÁLIDO! Digite apenas valores reais!\033[m')

#Armazenando os valores digitados na lista vendas efetuadas
      vendas_efetuadas.append(venda)

#Calculando o faturamento total da loja
faturamento = sum(vendas_efetuadas)
print(f'Faturamento total = R$ {faturamento:.2f}'.replace('.',','))

#Criando uma lista dos salários
salario = list()

#Calculando os salários dos vendedores e exibindo na tela
cont = 0
for i in vendas_efetuadas:
    cont += 1
    if i <= 5000:
        salario_vendedor = (i * 0.01) + salario_fixo_vendedor
        print(f'Salário do(a) {no_funcionario[cont-1]} = R$ {salario_vendedor:.2f}'.replace('.',','))

    elif i > 5000 and i <= 10000:
       salario_vendedor = (i * 0.015) + salario_fixo_vendedor
       print(f'Salário do(a) {no_funcionario[cont-1]}  = R$ {salario_vendedor:.2f}'.replace('.',','))
    
    elif i > 10000:
       salario_vendedor = (i * 0.02) + salario_fixo_vendedor
       print(f'Salário do(a) {no_funcionario[cont-1]}  = R$ {salario_vendedor:.2f}'.replace('.',','))

#Armazenando os salarios dos vendedores na lista salário     
    salario.append(salario_vendedor)   

#Calculando salário do gerente e exibindo na tela
salario_gerente = (faturamento * 0.005) + salario_fixo_gerente
print(f'Salário do(a) {no_gerente[0]} = R$ {salario_gerente:.2f}'.replace('.',','))

#Calculando salário total dos funcionários e exibindo na tela
salario_total_vendedor = sum(salario)   
salario_total = salario_total_vendedor + salario_gerente
print(f'Total dos salários = R$ {salario_total:.2f}'.replace('.',','))

        
