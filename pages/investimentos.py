import streamlit as st
import pandas as pd
import acesso_banco_de_dados as banco

# Inicializa uma lista vazia para armazenar os dados
data = []

@st.cache_data
def inicializar_dataframe():
    return pd.DataFrame(columns=["Investimento", "Valor", "Banco"])
st.set_page_config(page_title="PoupApp", layout="wide")
with open("teste.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

st.html("<h1 style='text-align: center'>Cadastro de Investimentos</h1>")

container = st.container(border=1)
opcoesInvestimentos = ['CDB','Tesouro Selic','FundosImobiliários','Ações','Fundos de Investimentos']
with container:
    investimento = st.selectbox("Selecione o tipo de investimento",opcoesInvestimentos)
    valor = st.number_input('Digite o valor do investimento')
    instituicao = st.text_input('Digite a instituição financeira')
    butao = st.button("Cadastrar")
    butao2 = st.button("Consultar")
    if butao:
        conexao = banco.abrir_conexao()
        cur = banco.abrir_cursor(conexao)
        banco.comando_insert_investimentos(cur, investimento, valor, instituicao)
        conexao.commit()  # Confirma a inserção no banco
        tabela = banco.comando_select_investimentos(cur, conexao)
        banco.fechar_conexao(cur, conexao)
        st.dataframe(tabela)
        st.success("Investimento cadastrado com sucesso!")

    if butao2:
        conexao = banco.abrir_conexao()
        cur = banco.abrir_cursor(conexao)
        tabela = banco.comando_select_investimentos(cur,conexao)
        banco.fechar_conexao(cur,conexao)
        st.dataframe(tabela)