#Python tem tipagem dinâmica 

x = 10 
print(type(x))
nome = 'Joaquim'
print(type(nome))

#Type hints ajuda a definir o tipo de dados esperado na variável 
#mas é apenas uma AJUDA, ou seja o python não impede que seja atribuido
#um valor com outro tipo de dados.

nome: str = 'Joaquim'
print(type(nome))

nome = 123
print(type(nome))

preco: float
preco = 7.8
print(type(preco))

#Todos os tipos de dados são aceitos no type hints
disponivel: bool = True
print(type(disponivel))

#O tipo de uso mais importante é quando definimos funções
#Quando definimos o tipo de dado esperado como parametro e tambem o 
#tipo de dados de retorno da fuunçao, estamos definindo a 
#assinatura da funçao, isso é imporatante para disponibilizarmos
#essas funções, por exemplo como API
def calcular_total(preco: float, quantidade:int) -> float:
    return preco * quantidade

print(calcular_total(preco, 2))
print(calcular_total(preco, 3))

#E quando a função nao tem retorno 
def exibir_produto(produto: str, preco: float) -> None:
    print(f"{produto} - {preco}")

exibir_produto('leite', 8.9)


#Revisão de List
#-> tipo de dados composto 
lista:list = ['café', 'ovo', 'carne']
print(lista)

dados = ['kim', 18, 'masculino']
print(dados)
print(f"Nome: {dados[0]}")
print(f"Idade: {dados[1]}")
dados.append ('estudante')
print(dados)
print('\nImprimindo elemente por elemento')
for item in dados:
    print(item)


def somar(precos: list) -> float:
    total = 0
    for preco in precos:
        total += preco
    return total
print("\nSomando preços ")
print(f'total: {somar([10, 20, 30])}')
def criar_produto(produto: str, preco: float, quantidade: int) -> list:
    return [produto, preco, quantidade]

print(f"Estoque: {criar_produto('leite', 8.9, 10)}")


#Tipos de dados genericos: object
#quando usar -> na assinatura da função 
#ebtebdimento 
#aqui estou criando uma lista que só aceita inteiros
idades: list[int] = [17, 54, 23]
print(f'Idadades: [idades]')

#mas se eu quisesse uma lista mista?
produto = ['camisa', 29.9, 8]
print(f'produto: [produto]')
#eu poderia lançar mao do objeto generico OBJECT
produto: list[object] = ['camisa', 29.9, 8]





def calcular_total(preco: float, quantidade: int) -> float:
    ###Calcula a quantidade total de um produto 

    #Args:
    #param preco: preço unitario do produto
    #param quantidade: quantidade total de um produto


    #Returns:
        #:return total: preco total (preco*quantidade)


    return preco * quantidade