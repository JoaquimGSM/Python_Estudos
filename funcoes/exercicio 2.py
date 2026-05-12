#EX 2
lados = int(input('Digite o númeo de lados da sua forma geométrica: '))
def verificar(lados):
    if lados == 3:
        return 'É um triangulo'
    elif lados == 4:
        return 'É um quadrilátero'
    elif lados == 5:
        return 'É um pentágono'
    else:
        return 'Não existe'

print(f'A sua fomra geométrica: {verificar(lados)}')