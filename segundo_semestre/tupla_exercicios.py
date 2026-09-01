#1
print('\n1')
notas = (7.5, 8.0, 6.5, 9.0)
print(notas[0])
print(notas[-1])

#2
print('\n2')
numeros = (12, 45, 7, 23, 9, 31)
soma = 0
for n in numeros:
    soma += n
print(soma)

#3
print('\n3')
inteiros = (11, 42, 65, 2, 63, 14, 12, 76, 27)
def contar_pares(inteiros):
    contador = 0
    for n in inteiros:
        if n % 2 == 0:
            contador += 1
    return contador
resultado = contar_pares(inteiros)
print(resultado)

#4
print('\n4')
produtos_loja1 = ("Caneta", "Caderno", "Mochila")
produtos_loja2 = ("Estojo", "Régua") 
todas_tuplas = produtos_loja1 + produtos_loja2
print(todas_tuplas)

#5
print('\n5')
tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)    
print(tupla[0:4])
print(tupla[4:])
print(tupla[::-1])

#6
print('\n6')
varios_numeros = (4, 7, 12, 65, 23, 74, 13, 6, 98, 3, 24, 50)
maior = max(varios_numeros)
menor = min(varios_numeros)
maior_menor = (maior, menor)
print(maior_menor)

#7
print('\n7')
lista_nomes = ["Ana", "Bruno", "Carla"]
tupla_nomes = tuple(lista_nomes)
lista_novamente = list(tupla_nomes)
lista_novamente.append('Diego')
print(lista_novamente)

#8
print('\n8')
notas = ((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0))

def calcular_media(notas, indice):
    aluno = notas[indice]
    soma = sum(aluno)
    quantidade = len(aluno)
    media = soma / quantidade
    return media
resultado = calcular_media(notas, 0)
print(resultado)