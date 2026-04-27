# cont = 1
# pares = 0
# while cont <= 10:
#     numero = int(input("Digite um número: "))
#     if numero % 2 == 0:
#         pares += 1
#     cont += 1
# print(f'Quantidade de números pares é {pares}')

# cont = 1
# soma = 0
# while cont <= 10:
#     soma += cont
#     cont += 1
# print(f'A soma dos 10 primeiros números é {soma}')

# cont = 1
# while cont <= 20:
#     print(cont)
#     cont += 1

# cont = 1
# while cont <= 10:
#     numero = float(input("Digite um número: "))
#     dobro = numero * 2
#     print(f'O dobro de {numero} é {dobro}')
#     cont += 1

# cont = 1
# menor = 0
# while cont <= 15:
#     idade = int(input('Digite sua idade: '))
#     if idade <= 18:
#         menor += 1
#     cont += 1
# print(f'Quantidade de pessoas menores de idade é {menor}')

# cont = 1
# quantidade = 0
# while cont <= 10:
#     nm = float(input('Digite um número: '))
#     if 100 <= nm <= 200:
#         quantidade += 1
#     cont += 1
# print(f'Quantidadde de número entre 100 e 200 é {quantidade}')

# cont = 1 
# soma = 0
# while cont <= 15:
#     nm = float(input('Digite um número: '))
#     if nm % 2 != 0:
#         soma += nm
#     cont += 1
# print(f'A soma dos números ímpares é {soma}')

# soma = 0
# while True:
#     nm = float(input('Digite um número (0 faz o programa parar): '))
#     if nm == 0:
#         break
#     if nm > 0:
#         soma += nm
# print(f'A soma dos números positivos até zero é {soma}')

# while True:
#     v1 = float(input('Digite o valor 1: '))
#     v2 = float(input('Digite o valor 2: '))
#     if v1 != v2:
#         break
#     else:
#         print('Os valores devem ser diferentes. Repita novamente.')

# if v1 > v2:
#     maior = v1
#     menor = v2
# else:
#     maior = v2
#     menor = v1  

# diferenca = maior - menor
# print(f'A diferença entre o maior e o menor valor é {diferenca}')

# cont = 1 
# menor = float('inf')  
# while cont <= 10:
#     nm = float(input('Digite umnúmero: '))
#     if nm < menor:
#         menor = nm
#     cont += 1
# print(f'O menor número digitado foi {menor}')

# n = int(input('Quantos número deseja digitar? '))

# soma_pares = 0
# qntd_pares = 0

# soma_impares = 0
# qntd_impares = 0

# for i in range(n):
#     numero = int(input('Digite um número: '))
#     if numero % 2 == 0:
#         soma_pares += numero
#         qntd_pares += 1
#     else:
#         soma_impares += numero
#         qntd_impares += 1
# # Cálculo das médias
# if qntd_pares > 0:
#     media_pares = soma_pares / qntd_pares
# else:
#     media_pares = 0

# if qntd_impares > 0:
#     media_impares = soma_impares / qntd_impares
# else:
#     qntd_impares = 0
# print(f'Média dos números pares: {media_pares}')
# print(f'Média dos números ímpares: {media_impares}')

# chico = 1.50
# juca = 1.10
# n = 0
# while juca <= chico:
#     chico += 0.02
#     juca += 0.05
#     n += 1
# print(f'Juca levará {n} anos para ser mais alto que Chico.')

n = int(input('Digite um número: '))
soma = 0
for i in range(1, n + 1):
    soma += i / n
print(f'O valor de S é {soma}')

n = int(input('Digite um número: '))
fatorial = 1
cont = 1
while cont <= n:
    fatorial *= cont
    cont += 1
print(f'O fatorial de {n} é {fatorial}')

