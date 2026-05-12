#Funções
#Sitanxe
# Def nome_Funcao(parametros separados por vírgula):
#   Instruções
#   Return expressão

#primeiro passo é a definição
#segundo passo é o uso da função 
print('Funçôes')
print('Função simples')
def OlaMundo ():
    print('Olá Mundo')

OlaMundo()
print('\nFunção com parametro e uso posicional')

def soma (p1, p2):
    total = p1 + p2

    print (total)

print('O total é:', end='')
soma(5,6)

print('\nFunção com parametro e uso nomeado')
def sub (p1, p2):
    total = p1 - p2
    print(total)
print('posicional')
print("O total é:", end='')
sub(5,3)

print('Nomeado')
print("O total é:", end='')
sub(p1 =5,p2 =3)

#ESCOPO
#No python e em qualquer linguagem ha uma discussão sobre o escopo que 
#É a visibilidade da variavel 
#Existem variaveis de escopo global e variaveis de escopo local:
#No escopo global as variaveis são definidas no programa principal
#EX 1 
# clima = 'inverno'
# def mostra():
# #Percebemos que mesmo dentro da função conseguimos acessar o 
# #valor da variavel clima
#     print(f'O clima de hoje é de {clima}')

# mostra()


# clima2 = 'inverno'
# def mostra2():

#     print(f'O clima de hoje é de {clima2}')

# #Se usarmos a função antes de definir a variavel global 
# #ela mostra um erro. 
# mostra2()
# clima2 = 'verão'

# #Em outras linguagens mesmo definindo a variavel antes
# #da chamada da função ela não funcionária  

#E se nós tivessemos uma variável que fosse definida dentro da função?
#Ou seja escopo local
#Será que consiguiriamos ver o valor dela no programa principal?

def mostraTemperatura ():
    temperatura = 13
    print(f'A temperatura hoje é de {temperatura}')

mostraTemperatura()

def defineTemperatura():
    #A variavel possui escopo local
    #ou seja, não conseguimos acessar seu valor
    #No programa principal
    temp = 14 

print(f'A temperatura é de {defineTemperatura}')



def soma2 (s1,s2):
    total = s1 + s2
    return total

s1 = 6
s2 = 9
print(f'A soma de de {s1} e {s2} é: {soma2(s1,s2)}')

def saudacao (nome):
    return "Bom dia" + nome + '!'

print(saudacao('Leticia'))