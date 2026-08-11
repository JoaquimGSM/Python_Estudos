# Funcoes: outros temas

# Parametros nomeados e posicionais

def calcular_media(python: float, webdev: float, frontend: float) -> float:
    return (python + webdev + frontend) / 3
"""
Calcula a média de três notas.
:param python: Nota em Python.
:param webdev: Nota em WebDev.
:param frontend: Nota em Frontend.

Args:
    python (float): Nota em Python.
    webdev (float): Nota em WebDev.
    frontend (float): Nota em Frontend.

Returns:
    float: A média das três notas.
"""

media = calcular_media(python=9, webdev=8, frontend=9.5)
print(f'Media: {media:.1f}')

#parametros nomeados
media = calcular_media(webdev=9, frontend=7, python=9.5)
print(f'Media: {media:.1f}')