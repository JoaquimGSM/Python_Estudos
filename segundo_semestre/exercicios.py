#1
titulo: str = 'Sapiens'
pagina: int = 457
preco: float = 70.0
print(f'O livro {titulo} possui {pagina} páginas e custa R${preco}!')

#//////////////////////////////////////////////////////////////////////////////////////////////

#2
def dobrar(numero: int) -> int:
    #Retorna o dobro do número recebido.
    return numero * 2

print(dobrar(20))

#//////////////////////////////////////////////////////////////////////////////////////////////

#3
def calcular_media(notas: list[float]) -> float:
    """
    Calcula a media das notas 

    Args:
        notas: Lista de notas 

    Returns:
        A média das notas 
    """

    return sum(notas) / len(notas)
print(calcular_media([7.8, 9.8, 8.7, 6.5, 4.5, 6.7]))

#//////////////////////////////////////////////////////////////////////////////////////////////

#4
def criar_aluno(nome: str, idade: int, curso: str) -> list[object]:
    """
    Cria uma lista com dados de um aluno

    Args:
        nome: Nome do aluno
        idade: idade do aluno
        curso: Curso do aluno 

    Returns:
        Uma lista no formato [nome, idade, curso]
    """
    return [nome, idade, curso]

print(criar_aluno('joaquim', 18, 'Engenharia de Software'))

#//////////////////////////////////////////////////////////////////////////////////////////////

#11
def reajuste (salario: float,) -> float:
    if salario > 2000:
        return salario * 1.07
    else:
        return salario * 1.15

salario_atual = float(input("Digite o seu salário: "))
print(f'R${reajuste} é o salario após o reajuste')
#//////////////////////////////////////////////////////////////////////////////////////////////

#11
def soma_divisores(numero: int) -> int:
    soma=0
    for num in range(1,numero+1):
        if numero % num == 0:
            soma+=num
    return soma
print(soma_divisores(6))