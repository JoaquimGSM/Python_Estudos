#1a cadastrar produto
#Parâmetros: catalogo, nome do produto, valor, quantidade
#Exemplo depois e cadastro 
#[['Camiste Azul', 89.90, 50], ['Cachecol', 35.00, 30]]

NOME = 0
PRECO = 1
ESTOQUE = 2


def cadastrar_produto(
    catalogo: list[list[object]],
    nome: str,
    preco: float,
    estoque: int
) -> list[list[object]]:


    produto = [nome, preco, estoque]

    catalogo.append(produto)

    return catalogo


def exibir_catalogo(catalogo: list[list[object]]) -> None:


    for produto in catalogo:
        print(
            f'{produto[NOME]} - '
            f'R$ {produto[PRECO]:.2f} '
            f'(estoque: {produto[ESTOQUE]})'
        )


if __name__ == "__main__":

    catalogo = []

    cadastrar_produto(
        catalogo,
        "Camiseta Azul",
        59.90,
        120
    )

    cadastrar_produto(
        catalogo,
        "Tênis Runner",
        199.90,
        40
    )

    exibir_catalogo(catalogo)
