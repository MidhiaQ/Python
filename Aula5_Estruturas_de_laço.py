#Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa
#Após isso o programa irá perguntar o nome de todas as pessoas e colocar em uma lista
#de covidados. Após irá imprimir todos os nomes da lista.

quantidade_pessoas = int (input("Quantas pessoas serão convidadas? "))
quantidade = []
for i in range(quantidade_pessoas):
    nome = input('Nome: ')
    quantidade.append(nome)

    print("Lista:")
for quantidades in quantidade: 
     print(quantidades)
    

