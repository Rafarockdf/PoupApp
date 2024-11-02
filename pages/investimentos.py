import streamlit as st



# Executa a função

st.set_page_config(page_title="PoupApp", layout="wide")
st.html("<h1 style='text-align: center'>Cadastro de Investimentos</h1>")
container = st.container(border=1)
opcoesInvestimentos = ['CDB','Tesouro Selic','FundosImobiliários','Ações','Fundos de Investimentos']
with container:
    st.selectbox("Selecione o tipo de investimento",opcoesInvestimentos)
    st.number_input('Digite o valor do investimento')
    st.text_input('Digite a instituição financeira')


