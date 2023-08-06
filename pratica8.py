#2. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando
#um automóvel que faz 12 quilômetros por litro. Para o cálculo, o usuário deve fornecer o
#tempo gasto e a velocidade média durante a viagem. Desta forma, será possível obter a
#distância percorrida com a fórmula:

#DISTANCIA ← VELOCIDADE × TEMPO.

#A partir do valor da distância, basta calcular a quantidade em litros de combustível utilizada
#na viagem com a fórmula:

#LITROS_USADOS ← DISTANCIA / 12.

#O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a
#distância percorrida e a quantidade de litros utilizados na viagem.

temp = float(input('Informe o tempo gasto na viagem:'))
velo = int(input('Informe a velocidade:'))

distancia = velo * temp
litros = distancia / 12

print(f'A velocidade media é: {velo}; O tempo gasto é: {temp}')
print(f'A distancia percorrida é: {distancia}; A quantidade de litros usados é: {litros:.2f}')
