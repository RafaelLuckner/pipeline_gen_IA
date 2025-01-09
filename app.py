import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time
import time as tm
from contrato import Vendas


def main():
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(tm.localtime().tm_hour, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    if st.button('Salvar'):

        data_hora = datetime.combine(data,hora)

        try: 
            venda = Vendas(email = email,
                    data = data_hora,
                    valor = valor,
                    quantidade = quantidade,
                    produto = produto)
            
            st.write(venda)
            
        except Exception as e :
            st.error(f'Erro ao salvar:  \n{e}')

        # st.write(f'Email: {email}')
        # st.write(f'data: {data_hora}')
        # st.write(f'Valor: {valor}')
        # st.write(f'Quantidade: {quantidade}')
        # st.write(f'Produto: {produto}')




if __name__ =='__main__':
    main()