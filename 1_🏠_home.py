import streamlit as st
import webbrowser
import pandas as pd

st.set_page_config(page_title="Portal da Transparência", page_icon="🏠", layout="wide")

if "data" not in st.session_state:
    df_data = pd.read_csv("output/tabela_final_2025.csv")
    st.session_state["data"] = df_data


st.markdown("# ANALISANDO O PORTAL DA TRANSPARÊNCIA 📊")
st.sidebar.markdown("Desenvolvido por [Juan Borinelli] (https://github.com/juan-borinelli)") #rodape com autoria e link de autor

st.markdown("""
Este projeto consiste em uma análise exploratória dos dados de viagens de servidores públicos federais em 2025, extraídos do **Portal da Transparência do Governo Federal**. \n
O Portal da Transparência disponibiliza publicamente dados sobre gastos do governo federal. Este projeto analisa especificamente a seção de viagens de servidores públicos do ano de 2025, buscando identificar padrões de gasto, órgãos com maior volume de viagens e possíveis anomalias nos dados.
\nAlém da análise em si, o projeto também serve como exercício prático de manipulação de dados reais e volumosos com **Pandas** e exibição de dados com **Streamlit**.""")

exb_tbl_int = st.checkbox("Exibir tabela completa") #checkbox para exibir ou não as tabelas
if exb_tbl_int:
    df_data = st.session_state["data"]
    st.write(df_data) 

btn = st.button('Arquivos do portal da transparência') #botao para abrir o link do portal da transparência
if btn:
    webbrowser.open_new_tab('https://portaldatransparencia.gov.br/download-de-dados/viagens')

btn2 = st.button('Repositório do projeto') #botao para abrir o link do repositório do projeto
if btn2:
    webbrowser.open_new_tab('https://github.com/juan-borinelli/analisando-dados-do-portal-da-transparencia')
