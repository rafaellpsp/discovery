import requests

# URL da API de consulta de CNPJ
cnpj = '60872306000160'
url = 'https://receitaws.com.br/v1/cnpj/'f'{cnpj}'

# Parâmetros da requisição (no caso de alguns serviços, você precisará passar o CNPJ como parâmetro)
#params = {'cnpj': '06102711000404'}

# Realizar a requisição GET
#response = requests.get(url, params=params)
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Extrair os dados da resposta (geralmente em formato JSON)
    data = response.json()
    # Criando Obj:
    obj = {
        'Loja':f'{data["fantasia"]}',
        'Endereço':f'{data["logradouro"]+" "+data["numero"]}',
        'Bairro':f'{data["bairro"]}',
        'Cidade':f'{data["municipio"]}',
        'UF':f'{data["uf"]}',
        'CEP':f'{data["cep"]}'
    }

    # Agora você pode manipular os dados conforme necessário
    print(obj)
else:
    # Se a requisição não for bem-sucedida, imprima o código de status para depuração
    print(f"Falha na requisição. Código de status: {response.status_code}")


