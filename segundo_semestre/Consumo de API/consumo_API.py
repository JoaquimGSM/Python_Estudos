#Consumo API 

#API serve para recuperarmos dados a aprtir de chamada de um programa
#Tipicamente esses "programas" estão disponiveis em algum url

##Nossa aplicação --> requisição para um servidor (API)
##Nossa aplicação <-- resposta

#Requisições são feitas através do REQUEST
#Quando usamos http usamos a biblioteca requests



#Para fazer a requisição usamos requests.get
#E recebemos a resposta com resposta.json

#Também temos o status a resposta
#resposta.status_code --> 200 ok, 404 file not found, 500 internal error

# import requests

# def consultar_cep():
#     try:
#         cep = input('Digite o CEP: ')

#         resposta = requests.get(f'http://viacep.com.br/ws/{cep}/json/')

#         if resposta.status_code == 200:
#             dados = resposta.json()

#             print(f'Logradouro: {dados["logradouro"]}')
#             print(f'Complemento: {dados["complemento"]}')
#             print(f'Bairro: {dados["bairro"]}')
#             print(f'Localidade: {dados["localidade"]}')
#             print(f'UF: {dados["uf"]}')

#         else:
#             raise Exception(f'Erro de requisição: {resposta.status_code}')

#     except requests.exceptions.ConnectionError:
#         print('Erro de conexão')

#     except Exception as e:
#         print(e)


# consultar_cep()


#Exercicio NASA
import requests

try:
    resposta = requests.get(
        'https://science.nasa.gov/wp-json/wp/v2/apod-basic',
        verify=False,
        timeout=10
    )

    resposta.raise_for_status()

    print(resposta.status_code)
    
    dados = resposta.json()
    if len(dados) > 0:
        imagem = dados[-1]

    print(f'Título: {imagem["title"]}')
    print(f'Data: {imagem["date"]}')
    print(f'Link da imagem: {imagem["hdurl"]}')

except requests.exceptions.ConnectionError:
    print("Erro de conexão.")

except requests.exceptions.HTTPError as erro:
    print(f"Erro HTTP: {erro}")

except requests.exceptions.Timeout:
    print("Tempo de resposta excedido.")

except requests.exceptions.RequestException as erro:
    print(f"Erro na requisição: {erro}")    