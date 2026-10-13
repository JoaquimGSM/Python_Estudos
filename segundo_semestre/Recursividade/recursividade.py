# Recursividade é a estratégia de quebrar um problema
# em partes menores até chegar a um problema conhecido.

# Ex: 5! = 5x4!, 4! = 4x3!, ... 1! = 1x0!, 0! = 1

# 0! é chamado de condição base.

# Fatorial com recursividade

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))

# Fazer uma função sem recursividade

lista = [3, 5, 678, 3, 78, 90]

def soma_lista_sem_recursao(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

print(soma_lista_sem_recursao(lista))

# Fazer uma função com recursividade

def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])

print(soma(lista))