import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from contrato import Vendas
import streamlit as st


load_dotenv()

# config DB

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def salvar_no_postgres(dado: Vendas):
    """
    Função para conexão e salvamento de informações no banco de dados
    """
    try:
        conn = psycopg2.connect(
            host = DB_HOST,
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )
        cursor = conn.cursor()

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query,
                    (dado.email,
                     dado.data,
                     dado.valor,
                     dado.quantidade,
                     dado.produto))
        
        conn.commit()
        cursor.close()
        conn.close()
        st.success('Dados salvos com sucesso no banco de dados ;)')

    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")