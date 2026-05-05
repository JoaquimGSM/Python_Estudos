#EXERCÍCIO 1
#
# par = []
# impar = []
#
# for i in range(10):
#     n = float(input('Digite um número: '))
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         impar.append(n)
#
# print(f'A sua lista de números pares é {par}')
# print(f'A sua lista de números impares é {impar}')
#

#EXERCÍCIO 2
lista = [1900]
par = []

for i in range(10):
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
        lista.append(n)
    else:
        lista.append(n)

media = sum(lista) / len(lista)
print(f'A média aritmética dos números da lista é: {media}')
soma_par = sum(par)
print(f'A soma dos números da lista par é: {soma_par}')





