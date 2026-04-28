titulo = 'Cadastro de uma lista'
print(f'{titulo:^30}')

#Lista vazia
numeros = []
#Cadastro com while True / Break
while True:
    nu = int(input('Digite um número os zero para sair: '))
    if nu == 0:
        break
    numeros.append(nu)
print(numeros)
#impeimir a coleção com os elementos lado a lado
#EX: 8,4,6,7
for item in numeros:
    print(item, end=', ')