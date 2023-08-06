#3. Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido
#em dólar (US$). O programa deve solicitar o valor da cotação do dólar e também a
#quantidade de dólares disponíveis com o usuário.

valor_dolar = float(input('Informe o valor do dólar atualmente: '))
quant = float(input('Informe quanto deseja converter: '))

cotacao = valor_dolar * quant

print('A cotação é: ', cotacao)
