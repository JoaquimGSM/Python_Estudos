#EX1
# lista = random.sample(range(1, 21), 10)
# print(lista)

# print()
# print()
# print()

#EX1
# import random
# num = []

# for i in range(10):
#     sorteado = random.randint(1, 20)
#     while sorteado in num:
#         sorteado = random.randint(1, 20)
#     num.append(sorteado)
# print(num)


#EX2
import random
numeros = []
for i in range(10):
    numeros.append(random.randint(1, 50))
print(numeros)
primos = []
for numero in numeros:
    primo = True 
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        primos.append(numero)
print(primos)
        




