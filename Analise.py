# Importando as bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Analise de Produtos',layout='wide')

# Mostrar na tela o botão que pede o arquivo
arquivo = st.file_uploader("Por favor anexe a tabela de produtos")

if arquivo == None:
    st.text("Por favor suba o arquivo")
else: 
    df = pd.read_excel(arquivo)

# Salvar as Métricas em variáveis 

    quantidade_produtos=len(df)
    total_kg = df["Peso_Kg"].sum()
    media_kg = df["Peso_Kg"].mean()

    # Exibir o título da página
    st.title("Produtos em estoque")

    # Filtro de dados 
    colFiltro1, colFiltro2 = st.columns(2)
    maisPesado = df['Peso_Kg'].max()

    with colFiltro1:
        minimo = st.number_input(label="Minimo",min_value=0,max_value=int(maisPesado))

    with colFiltro2:
        maximo = st.number_input(label='Maximo',min_value=0,max_value=int(maisPesado))


    # Previa dos dados 

    filtrado = df[(df['Peso_Kg']>minimo) & (df['Peso_Kg']<maximo)]
    st.dataframe(filtrado)


    # Exibir as métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Produtos: ",quantidade_produtos)
    col2.metric("Total em quilos ",total_kg)
    col3.metric("Média de peso do Produto",media_kg)

    # Fazer o agrupamento por categoria e contar o id_produto

    produto_categoria = df.groupby('Categoria')['ID_Produto'].count().reset_index()

    # Exibir o gráfico 

    st.bar_chart(data=produto_categoria,x='Categoria',y="ID_Produto")

    # Filtro de peso mínimo e peso máximo 

    peso_minimo = df.groupby('Peso_Kg').min
    peso_maximo = df.groupby('Peso_Kg').max
