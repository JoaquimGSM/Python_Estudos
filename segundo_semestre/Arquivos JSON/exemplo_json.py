# JSON
# Para tratar arquivos JSON o Python tem uma biblioteca própria

import json
import os

# Arquivos JSON são textos estruturados
print('\nJSON')

pessoa = {
    "nome": "Andrea",
    "idade": 56,
    "hobbies": ["tenis", "pilates"]
}

print(type(pessoa))
print(pessoa)

# A biblioteca json vai pegar esse dicionário e transformar em um texto
pessoa2 = json.dumps(pessoa)

print(type(pessoa2))
print(pessoa2)

# Gravando em arquivo JSON
with open('pessoa.json', 'w', encoding='utf-8') as arqvPessoa:
    json.dump(pessoa, arqvPessoa)
    arqvPessoa.write('\n')

# Gravando com indentação
with open('pessoa.json', 'a', encoding='utf-8') as arqvPessoa:
    json.dump(pessoa, arqvPessoa, indent=4)
    arqvPessoa.write('\n')

# Acentuação
pessoaNova = {
    'nome': 'Rogério',
    'idade': 56,
    'hobbies': ['Pilotar moto', 'Jogar tenis de tênis']
}

print('\nSem o parametro ensure_ascii')

pessoaNova2 = json.dumps(pessoaNova, indent=4)

print(type(pessoaNova2))
print(pessoaNova2)

print('\nCom o parametro ensure_ascii')

pessoaNova2 = json.dumps(
    pessoaNova,
    indent=4,
    ensure_ascii=False
)

print(type(pessoaNova2))
print(pessoaNova2)

# Gravando outro arquivo
with open('alunos3.json', 'w', encoding='utf-8') as arqvPessoa:
    json.dump(
        pessoaNova,
        arqvPessoa,
        indent=4,
        ensure_ascii=False
    )

# Leitura de JSON
print('\n\nLeitura de JSON')

# loads lê uma string JSON
pessoaTexto = '''
{
    "nome": "Joaquim",
    "idade": 18,
    "hobbies": ["Guitarra", "Boxe"]
}
'''

print(type(pessoaTexto))
print(pessoaTexto)

# Transformando string JSON em dicionário
pessoaDicionario = json.loads(pessoaTexto)

print(type(pessoaDicionario))
print(pessoaDicionario)

# Lendo um arquivo JSON que já existe
arquivo = 'alunos3.json'

if os.path.exists(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arqvPessoa:
        aluno = json.load(arqvPessoa)

        print(type(aluno))
        print(aluno)
else:
    print('Arquivo não encontrado')