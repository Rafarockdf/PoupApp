import requests
import json
import pandas as pd
from datetime import datetime, timedelta

def obter_taxa_selic():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados/ultimos/1?formato=json"
    response = requests.get(url)

    if response.status_code == 200:
        dados = json.loads(response.text)
        taxa_selic = dados[0]["valor"]
        data = dados[0]["data"]
        print(f"Taxa SELIC ({data}): {taxa_selic}%")
    else:
        print("Erro ao obter a taxa SELIC")
        

def ultimo_dia_util(data=None):
    # Use a data atual se nenhuma data for fornecida
    if data is None:
        data = datetime.now()
    else:
        data = datetime.strptime(data, "%Y-%m-%d")
    
    if data.weekday() == 5:  # Sábado
        data -= timedelta(days=1)
    elif data.weekday() == 6:  # Domingo
        data -= timedelta(days=2)
    
    return data.strftime("%Y-%m-%d")


def obter_taxa_cdi():
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4391/dados?formato=json'
    taxa = pd.read_json(url)
    taxa = pd.DataFrame(taxa)
    return taxa


def obter_ultima_taxa_cdi():
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4391/dados?formato=json'
    taxa_por_data = pd.read_json(url)
    taxa_por_data = pd.DataFrame(taxa_por_data)
    taxa_por_data = taxa_por_data.sort_values("data")
    valorIndex = taxa_por_data['valor'].count()
    ultimaTaxa = taxa_por_data['valor'][valorIndex-1]
    return ultimaTaxa