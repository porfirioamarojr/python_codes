import requests

url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)

dados = req.json()
print(dados)

val_reais = float(input("Informe o valor em R$ a ser convertido\n"))
cotacao = dados(['rates']['BRL'])
print(f'R${val_reais} em dólar valem US$ {(val_reais/cotacao):.2f}')