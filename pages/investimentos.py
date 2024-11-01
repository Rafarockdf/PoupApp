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
        print(f"Taxa SELIC ({data}): {taxa_selic}%")
    else:
        print("Erro ao obter a taxa SELIC")

# Executa a função

st.set_page_config(page_title="PoupApp", layout="wide")
st.html("<h1 style='text-align: center'>Cadastro de Investimentos</h1>")
container = st.container(border=1)
opcoesInvestimentos = ['CDB','Tesouro Selic','FundosImobiliários','Ações','Fundos de Investimentos']
with container:
    st.selectbox("Selecione o tipo de investimento",opcoesInvestimentos)
    st.number_input('Digite o valor do investimento')
    st.text_input('Digite a instituição financeira')

st.write(obter_taxa_selic())
