#Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do Exercito
#Para entrar no exercito é preciso ter mais de 18 anos, pesar mais ou igual a 60 kilos e medir mais ou igual a 1.70 metros

idade = input('Informe sua idade:\n')
if idade >= '18':
    print('Próximo\n')
else:
    print('Não foi possível passar para a próxima etapa\n')

peso = input('Informe seu peso:\n')    
if peso >= '60':
    print('Próximo\n')
else:
    print('Não foi possível passar para a próxima etapa\n')

altura = input('Informe sua altura:\n')    
if altura >= '1.70':
    print('Parabéns, você passou em todas as etapas!\n')
else:
    print('Não foi possível passar para a próxima etapa\n')               
