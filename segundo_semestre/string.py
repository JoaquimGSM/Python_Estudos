#String se comporta como se fosse uma lista 
#são uma sequencia de caracteres 

frase = 'Eu amo Python'
print(frase)
lista = frase.split()
print(lista)

primeira_palavra = lista[0]
print(primeira_palavra)
letra = primeira_palavra[0]
print(letra)

for palavra in frase.split():
    print(palavra)

for letra in frase:
    print(letra)

if 'python' in frase:
    print('Tem Python na frase')


print('\nSlicing de uma frase - dividindo em palavras')
frase = 'Eu amo Python'
lista_palavras = frase.split()
print(lista_palavras)

amor = lista_palavras[0:2]
print(amor)

print('\nSlicing de uma frase - dividindo em letras')
frase = 'Eu amo Python'
print(frase[0:2])