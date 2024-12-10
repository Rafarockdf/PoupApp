import psycopg2
import pandas as pd
def abrir_conexao():
    conexao = psycopg2.connect(database = "poupapp",
                            host = "localhost",
                            user = "postgres",
                            password = "rafa7887",
                            port = "5432")
    #print(conexao.info())
    return conexao

def abrir_cursor(conexao):
    cur = conexao.cursor()
    return cur

def comando_insert_investimentos(cur,investimento,valor,instituicao):
    insert = "INSERT INTO INVESTIMENTOS(tp_investimento , valor, instituicao) VALUES (%s,%s,%s)"
    cur.execute(insert,(investimento,valor,instituicao))
    

def comando_select_investimentos(cur,conexao):
    select = "SELECT * FROM INVESTIMENTOS"
    #consulta = cur.execute(select)
    consulta_df = pd.read_sql(select,conexao)
    return consulta_df
def fechar_conexao(cur,conexao):
    cur.close()
    conexao.close()
