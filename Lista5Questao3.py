#3. Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de
#vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15%
#de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês,
#com duas casas decimais.

nome = input("Informe seu nome: ")

salario = float(input("Informe seu salario: "))

vendas = float(input("Informe o total de vendas efetuadas no mes em dinheiro: "))

total = (salario+0.15*vendas)

print(f"O vendedor recebera {total:.2f}")
