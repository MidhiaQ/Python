#4. Faça um programa que receba o valor do salário de um funcionário e o valor do
#salário mínimo, calcule e imprima quantos salários mínimos o funcionário recebe.

valorsalario = float(input("Informe o seu salario atual: "))
salariominimo = float(input("Informe quanto e um salario minimo: "))

total = valorsalario/salariominimo

print(f"O funcionario recebe {total:.1f} salarios minimos por mes")
