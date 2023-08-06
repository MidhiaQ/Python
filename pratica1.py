#Fazer um programa para ler dois números inteiros, calcular e imprimir:
#a) A soma dos dois números
#b) A subtração do primeiro pelo segundo
#c) A multiplicação dos dois números
#d) A divisão do primeiro número pelo segundo
#e) O resto da divisão do primeiro pelo segundo
#f) O primeiro número elevado ao quadrado

num1 = int(input('Digite o primeiro numero:\n'))
num2 = int(input('Digite o segundo numero:\n'))

print('Soma:', (num1 + num2))
print('Subtracao',(num1 - num2))
print('Multiplicacao:', (num1 * num2))
print('Divisao:', (num1 / num2))
print('Resto da divisao:', (num1 % num2))
print('O primeiro elevado ao quadrado:', (num1 ** 2))
