import psycopg2
from psycopg2 import sql
from contract import Sells
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def save_on_postgres(data: Sells):
    """
    Função para salvar no postgres

    Args:
      email (EmailStr): E-mail do vendedor
      date_time (datetime): Data da venda realizada
      value (PositiveFloat): Valor da venda
      quantity (PositiveInt): Quantidade de produtos vendidos
      product (str): Produto vendido
    """

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        # Inserção dos data na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO sells (email, date_time, value, quantity, product) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            data.email,
            data.date_time,
            data.value,
            data.quantity,
            data.product
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")