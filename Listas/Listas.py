titulo = "Lista: printicpais funções"


minhaLista = [] #lista

#acrescentar valores na lista
minhaLista.append ('Café')
#Lista permite valores heterogeneos 
minhaLista.append (12)

print(minhaLista[1])

#Juntando suas listas (com extend)
complemento = ["Amor", "Felicidade", "Alegria"]
print('\n')
print(complemento)

#Acrescenta os elementos da lista complento a minhalista
minhaLista.extend(complemento)
print(minhaLista)

#Localizando um elemento e recuperando índice
print(f'A Alegria esta na posição: {minhaLista.index('Alegria')}')

#Removendo pelo índice
minhaLista.pop(4)
print(minhaLista)

#Rmovendo pelo nome 
minhaLista.remove(12)
print(minhaLista)

#Alterando o conteúdo de um elemento
minhaLista[0] = 'CAFÉ'
print(minhaLista)

#Inserindo um elemnto em uma deterinada posição
minhaLista.insert(2, 'Fúria')

#Ordenação de Lista
print('\nOrdenação com função nativa do Python')
print(minhaLista)
print(sorted(minhaLista))

print('\nOrdenação com método de classe List')
print(minhaLista)
minhaLista.sort()
print(minhaLista)

num = [4, 73, 54, 2, 4 , 6, 8, 235 ,7 ,345 ,78]
print(sorted(num))
print(num)
num.sort()
print(num)
#REVENSA
num.sort(reverse=True)
print(num)
print(f'Quatos zeros tem na lista: {num.count(4)}')
print(f'Onde está o primeiro quatro da lista: {num.index(4)}')

if num.count(4) >= 2:
    primeiro = num.index(4)
    segundo = num.index(4, primeiro + 1)
    print(f'O segundo quatro está na posição: {segundo}')
else:
    print("Não existe segundo 4")
