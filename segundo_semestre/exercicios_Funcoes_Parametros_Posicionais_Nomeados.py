#1
def mostrar_informacoes(nome: str, idade: int, cidade: str) -> None:
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Cidade: {cidade}")

mostrar_informacoes(nome="João", idade=25, cidade="São Paulo")

#2
def calcular_area_retangulo(base: float = 1.0, altura: float = 1.0) -> float:
    return base * altura

print(calcular_area_retangulo(base=5.0, altura=3.0))

#3
def soma(a:float, b:float) -> float:
    return a + b

print(soma(2.5, 4.75))

#4
def enviar_email(destinatario:str, assunto:str = "Sem Assunto", corpo:str = "") -> None:
    print(f"Enviando email para: {destinatario}")
    print(f"Assunto: {assunto}")
    print(f"Corpo: {corpo}")

enviar_email(destinatario="joaquim@gmail.com",
             assunto="Reunião",
             corpo="Olá, gostaria de marcar uma reunião para discutirmos o projeto.")


#5
def concatenar_strings(str1: str = "", separador: str = " ", str2: str = "") -> str:
    return str1 + separador + str2

print(concatenar_strings(str1="Bom", str2="dia!"))

#6
def comprar_produto(produto: str = 'Produto desconhecido', quantidade: int = 1) -> str:
    return f"Você comprou {quantidade} unidade(s) de {produto}."

print(comprar_produto(produto="Computador", quantidade=2))


#7
def mostrar_itens(itens: list[str]) -> None:
    for item in itens:
        print(item)

mostrar_itens(itens=['Arroz', 'Feijão', 'Macarrão'])