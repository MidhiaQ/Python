#Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular,
#utilizando a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA

print('Volume de uma caixa retangular')

comp = float(input('Informe o comprimento:'))
lar = float(input('Informe a largura:'))
altu = float(input('Informe a altura:'))

volume = (comp * lar * altu)

print('O volume é: ', volume)
