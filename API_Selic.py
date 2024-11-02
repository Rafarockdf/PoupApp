import requests
import json

def obter_taxa_selic():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"
    response = requests.get(url)

    if response.status_code == 200:
        dados = json.loads(response.text)
        taxa_selic = dados[0]["valor"]
        data = dados[0]["data"]
        print(f"Taxa SELIC ({data}): {taxa_selic}%")
    else:
        print("Erro ao obter a taxa SELIC")



