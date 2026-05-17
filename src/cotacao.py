import requests

def obter_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        cotacao = dados["USDBRL"]["bid"]

        return cotacao

    return None

print(obter_cotacao_dolar())