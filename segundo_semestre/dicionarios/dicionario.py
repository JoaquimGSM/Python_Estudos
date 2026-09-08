# #Dicionários são coleções do tipo formulário
# #chave: valor

# #Exemplo
# #Nome: Joaquim
# #Idade: 18
# #Sexo: Masculino
# # Nao são posicionais - Nao tem indice
# #Permitem tipos de dados diferentes
# #Permitem valores repetidos, porem chaves sao unicas
# #Permitem inclusao, alteração, exclusão são mutaveis
# #Símbolo = {}


# aluno = {'nome': 'Joaquim', 'idade': 18, 'sexo': 'Masculino'}
# print(aluno)
# print(type(aluno))

# print('Acessando valor a valor')
# print(aluno['nome'])
# print(aluno['idade'])
# print(aluno['sexo'])

# print('Dicionário vazio')
# vazio = {}
# print(vazio)

# print('\nAcessando valores em um dicionário')
# vazio['categoria'] = 'Brinquedos'
# print(vazio)
# print('\n')
# aluno['profissao'] = 'Estagioario'
# print(aluno)

# print('\nalterando valores')
# aluno['nome'] = 'Andréa'
# print(aluno)
# print(aluno.get('nome'))
# aluno.update({'idade': 19})

# print('\nRemovendo valores')
# aluno.pop('idade') 
# print(aluno)
# aluno.popitem()
# print(aluno)
# del aluno['sexo']
# print(aluno)

# print('\nlimpa o Dicionário')
# aluno.clear()
# print(aluno)


# print('\nPercorrendo ou varrendo o dicionário')
# aluno = {'nome': 'Andrea', 'idade': 18, 'sexo': 'feminino', 'profissao carteira': 'analista'}
# for característica in aluno:  # qdo só coloco o nome do dicionário estou pegando as chaves
#     print(característica)

# print('\nSomente as chaves')
# for chave in aluno.keys():
#     print(chave)
# print('\nSomente os valores')
# for valor in aluno.value():
#     print(valor)
# print('\nSomente os valores pelas chaves')
# for chave in aluno:
#     print(aluno[chave])

# print('\nOs itens completos')
# for item in aluno.itens():
#     print(item)

# print('\nOs itens ja separados com atribuição multiplas')
# for chave, valor in aluno.items():
#     print(f'{chave}={valor}')

# #Atribuição multipla
# x, y, z = 0, 1, 2   
# print(f'{x}')
# print(f'{y}')
# print(f'{z}')

# #Na maior parte das coleções a copia se da pela igualdade
# #Vamos examinar a lista
# original = ['café', 'pão', 'leite']
# copia = original
# print('original', original)
# print('copia  ', copia)
# copia.append('cachorro')
# print('original', original)
# print('copia  ', copia)

# print('\n\nCopiando dicionario')
# aluno = {'nome': 'Andrea', 'idade': 18, 'sexo': 'feminino', 'profissao carteira': 'analista'}
# copia_aluno = aluno.copy()
# print(copia_aluno)

# copia_aluno.update({'aluno' : 'Andrea Moura'})
# copia_aluno['nome'] = 'Andréa moura'
# print(copia_aluno)




#EXCEÇÕES
#São erros que acontecem no tempo de excucao de um programa

print('Eceções')
#Progrma base
print('\nTicket médio spermercado')
valor = float(input('Digite um valor gasto na compra: '))
qtde = int(input('Digite a quantidade de itens comprados:'))
ticket_medio = valor / qtde
print(f'O seu ticket médio é R${ticket_medio:.2f}')



print('\nTicket medio supermercado - com tratamento de erro especifico')
try:
    valor = float(input('Digite um valor gasto na compra: '))
    qtde = int(input('Digite a quantidade de itens da compra: '))
    ticket_medio = valor / qtde
    print(f'O seu ticket medio é R${ticket_medio:.2f}')
# except ZeroDivisionError:
#     print('Quantidade zerada')
except ValueError:
    print('Valor invalido')
except Exception as e: 
    print('Ocorreu um erro')





print('\nTicket medio supermercado - com tratamento de erro especifico else e finally')
try:
    valor = float(input('Digite um valor gasto na compra: '))
    qtde = int(input('Digite a quantidade de itens da compra: '))
    ticket_medio = valor / qtde
except ValueError:
    print('Valor invalido')
except Exception as e:
    print(f'Ocorreu um erro, contate o administrador: {e}')
else:
    print(f'o seu ticket médio é R${ticket_medio:.2f}')
finally:
    print('Obrigada por comprar no supermercado BEM BARATO')