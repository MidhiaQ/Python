#1. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo;
#b) a soma do triplo do primeiro com o terceiro;
#c) o terceiro elevado ao cubo.

print('Informe dois numeros inteiros e um real:')

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = float(input('Digite o terceiro numero:'))

print('O produto do dobro do primeiro com metade do segundo e:', (n1*2)*(n2/2))

print('a soma do triplo do primeiro com o terceiro e:', ((n1*3)+n3))

print('o terceiro elevado ao cubo e:', n3**3)
