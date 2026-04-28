#Há uma outra estrutura de repetição qeu serve para
#quando sabemos de antemão quantas repetições vamos ter
#FOR
#Percorre elementos iteraveis

# titulo ='Estrutura de repetição FOR'
# print(f'{titulo:^30}')
# titulo ='TABUADA'
# print(f'{titulo:^30}')
# #Enquando o while nos temos que controlar o contador
# #o for faz isso de maneira automatica
# n = int(input('Digite um número inteiro para a tabuada: '))
# for numero in (1,2,3,4,5,6,7,8,9,10): #O número representa o contador
#     tabuada = n * numero
#     print(f'{n} X {numero} = {tabuada}')
#

#Eciste uma maneira de abreviar essa lista de números
#O comando RANGE
#range nada mais é que um gerador de números de um intervalo
#Maniea de usar
print('Gerando 5 números')
for i in range(5):
    print(i)
print('\n')
for i in range(5):
    print(i+1)
print('\n')
for i in range(1,5):
    print(i)
print('\n')
for i in range(1,6):
    print(i)
print('\n')
for i in range(1,5+1):
    print(i)
print('\n')

#EXISTE MAIS UM PARAMETRO NO RANGE(PULO)

for i in range(1,5+1,2):
    print(i)
print('\n')

