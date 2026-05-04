# calculadora
def soma(a, b):
    return a + b
def sub(a,b):
    return(a - b)
def mult(a, b):
    return( a * b)
def div(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return(a / b)


a = float(input('Digite o primeiro número que deseja utlizar no seu cálculo:'))
print()
b = float(input('Digite o segundo número que deseja utlizar no seu cálculo:'))
print()

while True:
    selecao = input('Digite a operação que deseja realizar\n(soma, sub, mult, div ou sair caso queira terminar seus cálculos): ')
    print()
    if selecao == 'sair':
        print('Obrigado por testar a minha calculadora! ())._.))')
        break
    elif selecao == 'soma':
        print(f'O resultado da soma é: {soma(a, b)}')
        break
    elif selecao == 'sub':
        print(f' O resultado da subtração é: {sub(a, b)}')
        break
    elif selecao == 'mult':
        print(f'O resultado da multiplicação é: {mult(a, b)}')
        break
    elif selecao == 'div':
        print(f'O resultado da divisão é: {div(a, b)}')
        break
    else:
        print('Você fez tudo errado, então repita! Burro')
        continue