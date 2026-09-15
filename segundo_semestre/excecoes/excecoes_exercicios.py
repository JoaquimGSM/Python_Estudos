#1
# try: 
#     numero = int(input('Digite um número: '))
# except ValueError:
#     print('Digite um número inteiro!')

# else:
#     print(f'{numero} * {numero} = {numero * numero}')


#2
# try:
#     n1 = float(input('Digite um número: '))
#     n2 = float(input('Digite um número: '))

#     if n1 == n2:
#         raise ValueError('Os números são iguais!')

#     if n1 > n2:
#         print(f'{n1} é o maior')
#         print(f'{n2} é o menor')
#     else:
#         print(f'{n2} é o maior')
#         print(f'{n1} é o menor')

# except ValueError as erro:
#     print(f'Erro: {erro}')


#3
# try:
#     letra = str(input('Digite uma letra entre A, B, C ou D: '))

#     if letra not in ('A', 'B', 'C', 'D'):
#         raise ValueError('Letra incorreta')

#     match letra:
#         case 'A':
#             print('Ameixa')
#         case 'B':
#             print('Banana')
#         case 'C':
#             print('Carambola')
#         case 'D':
#             print('Damasco')

# except ValueError as errinho:
#     print(f"Erro: {errinho}")


#4
#Salários:
# sal_min = 1671
# salario = 7580

# try:
#     if sal_min < 0:
#         raise ValueError('Valor incorreto, pois é negativo')

#     if salario < 0:
#         raise ValueError('Valor incorreto, pois é negativo')

#     calculo = salario / sal_min

#     if calculo < 1:
#         print('Salário abaixo do mínimo')

#     else:
#         print(f'O salário de R$ {salario:.2f} corresponde a {calculo:.2f} salários mínimos.')

# except ZeroDivisionError:
#     print('Erro: o salário mínimo não pode ser zero.')

# except ValueError as erro:
#     print(f'Erro: {erro}')


#5
# def buscar_item_por_indice(lista: list[str], indice: int) -> str:
#     return lista[indice]

# produtos = ['Camiseta', 'Tênis', 'Boné', 'Mochila']

# try:
#     indice = int(input('Digite o índice do produto: '))
#     produto = buscar_item_por_indice(produtos, indice)
#     print(f'Produto em promoção: {produto}')
# except ValueError:
#     print('Erro: digite um número inteiro.')
# except IndexError:
#     print('Erro: essa posição não existe na lista.')


#6
# produtos = {
#     'camiseta': 50.00,
#     'tenis': 200.00,
#     'bone': 35.00
# }
# try:
#     nome = input('Digite o nome do produto: ').lower()
#     preco = produtos[nome]
#     print(f'O preço de {nome} é R$ {preco:.2f}')
# except KeyError:
#     print('Erro: produto não cadastrado.')


# #7
# try:
#     n1 = float(input('Digite o primeiro número: '))
#     n2 = float(input('Digite o segundo número: '))
#     media = (n1 + n2) / 2
# except ValueError:
#     print('Erro: digite apenas números.')
# else:
#     print(f'Média: {media:.2f}')
#     print('Cálculo realizado com sucesso!')
# finally:
#     print('Cálculo finalizado.')


# #8
# produto = input('Digite o nome do produto: ')

# try:
#     estoque = int(input('Digite a quantidade disponível em estoque: '))
#     quantidade = int(input('Digite a quantidade que deseja comprar: '))
# except ValueError as erro_conversao:
#     print(f'Erro de conversão: {erro_conversao}')
# else:
#     try:
#         if quantidade > estoque:
#             raise ValueError('Quantidade desejada maior que o estoque disponível.')
#         print(f'Compra de {quantidade} unidade(s) de {produto} realizada com sucesso.')
#     except ValueError as erro_estoque:
#         print(f'Erro de estoque: {erro_estoque}')