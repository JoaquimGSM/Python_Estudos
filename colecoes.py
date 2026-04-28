#Coleção
#
# São variáveis de memoria que tem multiplos valores
# Cada valor é cahamado de item ou elemento que podem ser do mesmo tipo de dado ou de tipos
# diferentes:homogeneos ou heterogeneos respectivamente
#
# TODA coleção é um elemento ITERAVEL
# significa que pode ir de um em um
# que é percorriel
#
# Há vários tipos e coleções:LISTAS, CONJUNTOS, DUPLAS, DICIONÁRIOS(formulário, chave/valor)


#Lista
#Características
#poderosa, flexível, performática, conjunto de comando para manipulação completos
#Mutável: Depois de criada a lista permite acrescentar retirar e modificar elementos
#ESpansivel: Pode aumentar seu conjunto de dados a partir de outra lista
#Aceita tipos diferentes de dados
#inexada: Cada elemento tem uma posilçao dentro da lista
#Permite duplicados
#Ordenáveis ==> A ordenação natural só acontece se todos os elementos forem do mesmo tipo

titulo = "Listas"
print(f'{titulo:^30}')
minhaLista=['café', 'água', 'açucar']
print(minhaLista)

#E se eu quisesse imprimir apenas o café
#Vamos acessar cada elemento pelo índice
#Toda coleção indexada começa no zero

             0       1         2        3         4
            -5        -4       -3       -2         -1
minhaLista=['café', 'água', 'açucar', 'canela', 'café']


print(f'Primeiro elemento: {minhaLista[0]}')
print(f'tamanho da lista: {len(minhaLista)}')
print(f'ultimo elemento: {minhaLista[4]}')
print(f'ultimo elemento: {minhaLista[len(minhaLista)-1]}')

#tentando acessar um indice que não eiste
# print(f'ultimo elemento: {minhaLista[5]}')

#Como acrescentar itens em uma lista?
#É o método append faz isso
print('\n')
print(minhaLista)
minhaLista.append('chantilly')
minhaLista.append('especiarias')
print(minhaLista)

#E para remover itens da lista
#Usamos o método pop
#Ele sem parâmetro remove do fim da lista
minhaLista.pop()
print(minhaLista)

#Mas eu posso remover um item específico com o pop
#Basta passar o indice
#removendo o açucar
minhaLista.pop(2)
print(minhaLista)

#TODO ELEMENTO iterável podemos percorrer através do pdr
print('Elementos um a um')
for item in minhaLista:
    print(item)
print('\n')
#Percorrendo a lista pelos indices da lista
for i in range(len(minhaLista)):
    print(minhaLista[i])


