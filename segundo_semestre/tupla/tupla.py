#Tupla
#é também uma coleção
#ela é IMUTAVEL. GABRIELA - nasce e morre do mesmo jeito
#ela é indexida (POSICIONAL), ela é heterogenea


print('TUPLA')
minhaTupla = ('sol', 'agua', 'natureza')
#minhaTupla = ('sol', 'agua', 'natureza')
##               0       1         2 
##              -3      -2        -1
print(minhaTupla)

print('\nTipos de dados diferentes')
outraTupla = tuple(('a', 45, True))
print(type(outraTupla))
print(outraTupla)

print('\nAcessando pela posição')
print(f'1º posição: {minhaTupla[0]}')
print(f'2º posição: {minhaTupla[1]}')

print('\nPegadinha')
#Não faz sentido pois você nao ira poder mudar a Tupla
tuplaVazia = ()
print(tuplaVazia)

print('\nPegadinha 2 - Tuple de um elemento precisa de virgula')
tuplaUm = ('Sol')
print(tuplaUm)
print(type(tuplaUm))

tuplaUmReal = ('Sol',)
print(tuplaUmReal)
print(type(tuplaUmReal))

print('\nAchando a posição de um elemento')
minhaTupla = ('sol', 'agua', 'natureza', 'sol')
print(minhaTupla)
print(f'A água esta na posição: {minhaTupla.index('agua')}')
print(f'O 1° sol esta na posição: {minhaTupla.index('sol')}')
print(f'O próximo sol esta na posição: {minhaTupla.index('sol', 1)}')   


minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(f'O 1o sol esta na posicao: {minhaTupla.index("sol")}')
print(f'O 2o sol esta na posicao: {minhaTupla.index("sol", minhaTupla.index("sol") + 1)}')
# a partir da 2a ocorre
print(f'O 3o sol esta na posicao: {minhaTupla.index("sol", minhaTupla.index("sol", minhaTupla.index("sol") + 1) + 1)}')


print('\nPercorrendo a colecao toda')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(minhaTupla)
for item in minhaTupla:
    print(item)
print('\nAchando a posicao dos sois')
# O enumerate traz o par (indice, item)
# E ai usamos a atribuição multipla do python para colocar nas respectivas variáveis
#for n, elemento in enumerate(minhaTupla):
for indice, item in enumerate(minhaTupla):
    if item == 'sol':
        print(f'Posição {indice}: {minhaTupla[indice]}')

print('\nMatriz de tuplas')
matrizTupla = (('café', 'doce'), ('carne', 'farinha'), ('fruta', 'feijão'))
print(matrizTupla)
print(matrizTupla[2][1])

#Unpacking - atribuicao multipla
pessoa = ('Patricia', 'Casada', 54)
nome, estado_civil, idade = pessoa
print(nome)
print(estado_civil)
print(idade)


print('\nConversao para gambiarra')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(minhaTupla)
# Acrescentar um elemento ???? nao tem append
# como fazer
temp = list(minhaTupla)
temp.append('chuva')
print(type(temp))
minhaTupla = tuple(temp)
print(minhaTupla)
del temp