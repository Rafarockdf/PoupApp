import streamlit as st
import requests
import json

def obter_taxa_selic():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"
    response = requests.get(url)

    if response.status_code == 200:
        dados = json.loads(response.text)
        taxa_selic = dados[0]["valor"]
        data = dados[0]["data"]
        return f"Taxa SELIC ({data}): {taxa_selic}%"
    else:
        return "Erro ao obter a taxa SELIC"

st.set_page_config(page_title="PoupApp", layout="wide")
st.html("<h1 style='text-align: center'>Digite suas Informações</h1>")
container = st.container(border=1) 
barraLateral = st.sidebar
with barraLateral:
    st.write('Páginas')
    st.page_link('pages/investimentos.py',label="Cadastro Investimentos", icon="1️⃣")
with container:
    st.text_input('Digite o nome do membro familiar')
    st.number_input('Digite o valor a ser investido')

st.write(obter_taxa_selic())

