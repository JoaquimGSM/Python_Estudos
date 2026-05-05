#EX1

# for i in range(1,50+1):
#     print(i)


#EX2

# for i in range(200,99,-1):
#     print(i)

#EX3
# impar = 0
# for i in range(1,100+1):
#     if i % 2 != 0:
#         impar += 1
# print(impar)


#EX4

# import random
# for i in range(20):
#     numero = random.randint(1,50)
#     print(numero)


#EX5

# import math
# cont = 1
# while cont <= 5:
#     n = float(input('Digite um número: '))
#     cont += 1
#     raiz = math.sqrt(n)
#     print(f'A raiz quadrada de {n} é {raiz:.2f}')


#EX6
# maior = None
# menor = None

# for i in range(10):
#     numero = int(input("Digite um número inteiro: "))

#     if maior is None or numero > maior:
#         maior = numero

#     if menor is None or numero < menor:
#         menor = numero

# print("Maior número:", maior)
# print("Menor número:", menor)


#EX7
# divisores = []
# n = int(input('Digite um número para analizarmos os seus divisores: '))
# for i in range(n + 1):
#     if i != 0 and n % i == 0:
#         divisores.append(i)
# print(f'Os divisores de {n} são: {divisores}')


#EX8

# n = int(input('Digite um número: '))

# primo = True
# if n < 2:
#     primo = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             primo = False
#             break
# if primo:
#     print(f'{n} é um número primo.')
# else:
#     print(f'{n} não é um número primo.')


#EX9

# n = int(input('Digite um número: '))
# fatorial = 1
# cont = 1
# while cont <= n:
#     fatorial *= cont
#     cont += 1
# print(f'O fatorial de {n} é {fatorial}')


#EX10
alunos = int(input("Quantidade de alunos: "))
qtd_notas = int(input("Quantidade de notas por aluno: "))

for i in range(alunos):
    soma = 0

    print(f"\nAluno {i + 1}")

    for j in range(qtd_notas):
        nota = float(input(f"Digite a nota {j + 1}: "))
        soma += nota

    media = soma / qtd_notas
    print(f"Média do aluno {i + 1}: {media:.2f}")