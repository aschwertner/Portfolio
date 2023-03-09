# Importação das bibliotecas
import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import yfinance as yf
yf.pdr_override()

# Criação do menu
st.sidebar.title('Menu')

# Listas das empresas, tickets da B3 e imagens
empresas = ['Banco do Brasil', 'Bradesco', 'BTG Pactual', 'Itaú Unibanco', 'Santander Brasil']
tickets = ['BBAS3.SA', 'BBDC4.SA', 'BPAC11.SA', 'ITUB4.SA', 'SANB11.SA']
imagens = [
    'imagens/bb.png',
    'imagens/bradesco.png',
    'imagens/btg.png',
    'imagens/itau.png',
    'imagens/santander.png'
]

# Seleção da empresa
selecao = st.sidebar.selectbox('Selecione a empresa: ', empresas)

# Quantidade de meses
range = st.sidebar.slider('Período de Meses: ', 0, 12, 1, key = 'barra_selecao')
selecao_range = str(range) + 'mo'

# Ticket e imagem da empresa selecionada
if selecao == empresas[0]:
    selecao_ticket = tickets[0]
    selecao_imagem = imagens[0]
elif selecao == empresas[1]:
    selecao_ticket = tickets[1]
    selecao_imagem = imagens[1]
elif selecao == empresas[2]:
    selecao_ticket = tickets[2]
    selecao_imagem = imagens[2]
elif selecao == empresas[3]:
    selecao_ticket = tickets[3]
    selecao_imagem = imagens[3]
else:
    selecao_ticket = tickets[4]
    selecao_imagem = imagens[4]

# Colunas
col1, col2 = st.columns([0.9, 0.1])

# Título
titulo = f'Análise Econômica {str(selecao_ticket)}'
col1.title(titulo)
col2.image(selecao_imagem, width = 70)

# Coletar os dados da API do Yahoo Finance
dados = web.get_data_yahoo(selecao_ticket, period = selecao_range)

grafico_candlestick = go.Figure(
    data = [
        go.Candlestick(
            x = dados.index,
            open = dados['Open'],
            high = dados['High'],
            low = dados['Low'],
            close = dados['Close']
        )
    ]
)

grafico_candlestick.update_layout(
    xaxis_rangeslider_visible = False,
    title = 'Análise das ações',
    xaxis_title = 'Período',
    yaxis_title = 'Preço'
)

# Mostra o gráfico do Plotly no Streamlit
st.plotly_chart(grafico_candlestick)

if st.checkbox('Mostrar dados da tabela'):
    st.subheader('Tabela de registros')
    st.write(dados)