# #1
# pessoas = {}
# for i in range(5):
#     cpf = input('Digite um cpf: ')
#     nome = input('Digite um nome: ')

#     pessoas[cpf] = nome

# print('Pessoas cadastradas')
# print(pessoas)


#2
# produtos = {}
# for i in range(5):
#     produto = input('Qual o nome do produto ')
#     preco = int(input('Qual o valor do produto'))    

#     produtos[produto] = preco

# print(produtos)

# for produto, preco in produtos.items():
#     if preco >= 50:
#         print(produto, preco)

#3
alunos = {}
for i in range(3):
    rm = input('Qual o RM: ')

    nota1 = float(input('Digite a nota: '))
    nota2 = float(input('Digite a nota: '))
    nota3 = float(input('Digite a nota: '))

    notas = [nota1, nota2, nota3]

    alunos[rm] = notas

    for rm, notas in alunos.items():
        media = sum(notas) / len(notas)
    print(rm, media)

print(alunos)

#4
texto = input("Digite um texto: ").lower()

vogais = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
for letra in texto:
    match letra:
        case "a":
            vogais["a"] += 1
        case "e":
            vogais["e"] += 1
        case "i":
            vogais["i"] += 1
        case "o":
            vogais["o"] += 1
        case "u":
            vogais["u"] += 1
print(vogais)