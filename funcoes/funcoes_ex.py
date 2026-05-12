# #EX exemplo
# def oi():
#     return 'Bom Dia!'
# def oi2():
#     return 'Boa Tarde!'
# def oi3():
#     return 'Boa Noite!'

# horario = int(input("Qual é o horário? "))

# if 6 <= horario < 12:
#     print(oi())

# elif 12 <= horario < 18:
#     print(oi2())
# else:
#     print(oi3())

# print('\n')
# print('\n')
# print('\n')

# #EX 1
# n1 = float(input("Digite sua nota na primeira matéria: "))
# n2 = float(input("Digite sua nota na segunda matéria: "))

# def media(n1, n2):
#     calculo = (n1 + n2) / 2
#     return calculo

# resultado = (media(n1, n2))

# if resultado >= 6:
#     print(f'Você foi aprovado!!! Sua meédia é: {resultado}')
# else:
#     print(f'Infelizmente você foi reprovado e sua média é: {resultado}')


# #EX 2
# lados = int(input('Digite o númeo de lados da sua forma geométrica: '))
# def verificar(lados):
#     if lados == 3:
#         print('É um triângulo')
#     elif lados == 4:
#         print('É um quadrilátero')
#     elif lados == 5:
#         print('É um pentágono')
#     else:
#         print('Valor inválido')


# #EX 3
# num = int(input('Digite um número: '))
# def dobro(num):
#     resultado = num * 2
#     return resultado
    

# print(f'O dobro de {num} é: {dobro(num)}')


# #EX 4
# num = int(input('Digite um número: '))
# def verifica(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# print(verifica(num))

raio = float(input('Digite o valor do raio: '))
def area(raio):
    resultado = (raio * raio) * 3.14
    return resultado

def perim(raio):
    resultado = raio * 3.14 * 2
    return resultado

print(f'O valor da área é: {area(raio)}')
print('\n')
print(f'O valor do perimetro é: {perim(raio)}')
