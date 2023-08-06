#Faça um programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas por semana. Calcule e mostre seu salário por semana.

ganho = float(input('Informe quanto ganha por hora:'))
horas = float(input('Informe as horas trabalhadas:'))

print(f'O salário por semana é {(ganho * horas): .3f}')
