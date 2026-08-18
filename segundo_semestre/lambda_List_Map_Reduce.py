print('/////////////LAMBDA///////////')
# #Função anonima (pequeo - de uma linha só - função inline)
# #A criação da função está próxima do uso 
# #Versáteirs
# #CUIDADO que temos que ter, é não tentar resolver tudo com lambda
# #Se vc fizer isso o seu programa fica ilegível

# #Em uma função tradicional fariamos assim:
# def dobro(n:int) -> int:
#     """
#     Calcula o dobro de um número inteiro

#     :param n: número inteiro
#     :return: dobro de um número inteiro
#     """
#     return n * 2

# #Transformar em lambda
# ldobro = lambda n : n * 2
# print(ldobro(80))

# print((lambda n : n * 3)(40))

# #Lambda condicional 
# #Tem um if embutido

# #Função que decide qual o maior dos dois números 
# #Transformando em Lambda
# lmaior = lambda x,y : x if x > y else y 
# print(lmaior(3,5))

# #uso mais comum 
# print((lambda x,y : x if x > y else y)(124,54))

# #Pode usar print dentro de lambda mas cuidado
# lmenor = lambda x,y: f"Entre {x} e {y} o número menor é {x}" if x < y else \
#         f"Entre {x} e {y} o número menor é {y}"
# print(lmenor(20,78))


# print('//////////////////////////EXERCÍCIOS////////////////////////////////')

# #2
# par_ou_impar = lambda n : f"o número {n} é par"  if n % 2 == 0 \
#             else f"o numero {n} é ímpar"
# print(par_ou_impar(42))


print('/////////////MAP///////////')

#Map é uma funcionalidade do python que permite aplicar 
#uma função em todos os elementos de uma coleção 
def dobro2 (n:int) -> int:
    return n * 2
numeros = [7, 4, 25, 68, 76, 34]

for n in numeros:
    print(dobro2(n))

#Com o MAP

print(list(map(dobro2, numeros)))



#O jeito mais pythoneiro
print(list(map(lambda n: n*3, [23, 4, 876, -4])))


#Desafio
precos = [100.0, 250.0, 39.90]
descontos = [0.1, 0.2, 0.05]

#RACIOAL, pegar um caso e fazer um DEF para resolver isso 
preco = 100
desconto = 0.1
def calculo_desconto(p, d):
    return p * (1 - d)
print(f'Com {desconto} de desconto meu preco R${preco:.2f} será '
      f'R${calculo_desconto(preco, desconto):.2f}')
precos = [100.0, 250.0, 39.90]
descontos = [0.1, 0.2, 0.05]
precos_descontos = list(map(calculo_desconto, precos, descontos))
print(precos)
print(precos_descontos)


#Exercício 4
def maiuscula(texto: str) -> str:
    return texto.upper()

nomes = ["ana", "bruno", "carla"]
print(list(map(maiuscula, nomes)))


#O jeito mais pythonico
print(list(map(lambda n: n * 3, [23, 4, 876, -4])))
#REDUCE:
#É uma funcao qe aplica um def ou lambda em todos elementos
#de uma colecao (lista) e rezuz a um único elemento

def soma (n: int, m: int) -> int:
    return n+m
print(soma(4,7))

import functools as f
numeros = [6, 34, 87, 23, 12, 32]
total = f.reduce(soma, numeros)
print(total)


#Exercício 5
def mult (n: int, m: int) -> int:
    return n * m
print(mult(4,7))
total1 = f.reduce(mult, numeros)
print(total1)


#Exercício 6
from functools import reduce
numeros = [15, 42, 8, 99, 23]
maior = reduce(lambda a, b: a if a > b else b, numeros)
print(maior)