#2. Faça um programa que receba a quantidade de pessoas vacinadas no primeiro dia do
#mês e calcule a estimativa de vacinação mensal (OBS: considere o mês com 22 dias úteis).

dia1 = int(input('Informe a quatidade de vacinas aplicadas no primeiro dia: '))

dias_uteis = 22

total = dia1 * dias_uteis

print(f"A estimativa e de {total} pessoas vacinadas no mes")
