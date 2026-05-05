#Matrizes são listas de listas 
#   1   2   3
#   4   5   6
#   7   8   9

print('MATRIZES')
matriz = [[1, 2 ,3],[4, 5, 6],[7,8,9]]
print(matriz)
# cada linha é um elemento na matriz principal
# Para acessar um elemento eu devo usar um par ordenado
# Par acessar o 5, sabemos que esta na linha 1 e coluna 1


print(f'Elemento do meio da matriz: {matriz[1][1]}')

#mudar um número
matriz[1][2] = 102
print(matriz)

#EX matriz 4x3
matriz = [[]]
from faker import Faker 
faker = Faker('pt-BR')
for i in range(4):
    linha = []

    for j in range(3):
        linha.append(faker.name())
    
    matriz.append(linha)
print(matriz)