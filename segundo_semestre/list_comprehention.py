# def mult (n: int, m: int) -> int:
#     return n * m

# numeros = [10, 23, 4, 53, 50]
# print(numeros)
# multiplicadores = [2, 4, 3, 12, 100]
# multiplicados = list(map(mult, numeros, multiplicadores))
# print(multiplicados)

# multiplicados2 = list(map((lambda m, n: n * m), numeros, multiplicadores))
# print(multiplicados)

# print('\n List Comprehention')
# #Feito para simplificar o map
# #Retorna uma lista
# print('\n Sem o list comprehention')
# numeros = [7, 54, 23, 763, 32]
# dobrados = []
# for n in numeros:
#     dobrados.append(n * 2)

# print(dobrados)

# print('\n Com o list comprehention')

# dobrados2 = [n * 2 for n in numeros] 
# print(dobrados2)

# print('\n EXERCÍCIO \n\n')
#////////////////////////////////////////////////////////////////////
#7 (1)
quadrados = [q ** 2 for q in range (1,11)]
print(quadrados) 

#8 (2)
print('\n')
numeros = [3, 8, 15, 22, 7, 40, 11]
so_pares = [numero_analisado for numero_analisado in numeros if numero_analisado % 2 == 0]
print(so_pares)


#EXEMPLO IF e ELSE
print('\n')
print('\nCom o list comprehension e condicional com else')
numeross = [7, -87, 90, -23, 4, 0]
dobrados_positivos_100_negativos = \
    [n * 2 if n > 0 else n+100 for n in numeross]
print(dobrados_positivos_100_negativos)

#9. Dada lista, crie um nova lista informando par ou impar
numeros = [3,8,15,22,7,40,11]


#10. Dada a lista de produtos, use list comprehension para criar uma
#list com os nomes e produtos com 
produtos = [

NOME
PRECO
ESTOQUE
produtos_abaixo_estoque = [prod[0] for prod in produtos if prod[ESTOQUE] < 100]
print(produtos_abaixo_estoque)