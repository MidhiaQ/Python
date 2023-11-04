#Crie uma lista e adcione 5 nomes, remova dois, insira um novo nome no meio da lista, conte se tem algum nome repetido
#print tudo normal e inversa e em seguida limpe a lista.

listaNome = ['Maria', 'João', 'Vivi', 'Pedro', 'Julia']
print(listaNome)

listaNome.remove ('Julia')
listaNome.remove ('Pedro')
print(listaNome)

listaNome.insert (2, 'Vivi')
print(listaNome)

contar = listaNome.count ('Vivi')
print('O nome se repete', contar, 'veze(s)')

print(listaNome)
print(listaNome[-1:-5:-1])

listaNome.clear
