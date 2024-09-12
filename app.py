import streamlit as st
from contract import Sells
from datetime import datetime, time
from pydantic import ValidationError
from database import save_on_postgres

def main():
  st.title("Sistema de CRM e Vendas - Front-end")

  email = st.text_input("E-mail do vendedor")
  date = st.date_input("Data da venda realizada", datetime.now())
  hour =  st.time_input("Hora da venda realizada", value=time(9, 30))
  value = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
  quantity = st.number_input("Quantidade de produtos vendidos", min_value=1, step=100)
  product = st.selectbox("Escolha o produto vendido", options=["Item 1", "Item 2", "Item 3"])

  if st.button("Salvar"):

    try:
      date_time = datetime.combine(date, hour)

      sell = Sells(email=email, date_time=date_time, value=value, quantity=quantity, product=product)

      # st.write("**Dados da Venda:**")
      # st.write("E-mail do vendedor:", email)
      # st.write("Horário da venda realizada:", date_time)
      # st.write("Valor da venda: R$", value)
      # st.write("Quantidade de produtos vendidos:", quantity)
      # st.write("Produto vendido:", product)
      # st.success("Cadastrado com sucesso!")

      st.write(sell)
      save_on_postgres(sell)
    except ValidationError as e:
      st.error(e.errors())

if __name__ == "__main__":
  main()