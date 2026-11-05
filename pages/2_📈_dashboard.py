import streamlit as st

df_data = st.session_state["data"]
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

cargos = df_data['Cargo'].unique().tolist()
cargo = st.sidebar.selectbox("cargo", cargos)

df_cargos = df_data[df_data['Cargo'] == cargo]

st.markdown("## Dashboard de Análise de Viagens 📊")
st.markdown("Este dashboard permite explorar os dados de viagens de servidores públicos federais em 2025, filtrando por cargo específico. \n\n")

lista_graficos = ["Número de viagens por órgão", "Gastos totais por órgão", "Gastos médios por viagem por órgão", "Distribuição de gastos por tipo de viagem"]

selected_grafico = st.selectbox("Selecione a tabela e gráfico desejados", lista_graficos)
if selected_grafico == "Número de viagens por órgão":
    st.markdown("### Gráfico 1: Número de viagens por órgão")
    st.markdown("Este gráfico mostra o número total de viagens realizadas por cada órgão do governo federal em 2025, filtrando pelo cargo selecionado. \n\n")
    df_data[df_data['Cargo'] == cargo][["Cargo", "n_viagens"]]


exb_all = st.checkbox("Exibir todos os gráficos interativos") #checkbox para exibir ou não os graficos interativos
if exb_all:
    st.markdown("### Gráfico 1: Número de viagens por órgão")
    st.markdown("Este gráfico mostra o número total de viagens realizadas por cada órgão do governo federal em 2025, filtrando pelo cargo selecionado. \n\n")
    st.markdown("### Gráfico 2: Gastos totais por órgão")
    st.markdown("Este gráfico apresenta os gastos totais com viagens por cada órgão do governo federal em 2025, filtrando pelo cargo selecionado. \n\n")
    st.markdown("### Gráfico 3: Gastos médios por viagem por órgão")
    st.markdown("Este gráfico mostra os gastos médios por viagem para cada órgão do governo federal em 2025, filtrando pelo cargo selecionado. \n\n")
    st.markdown("### Gráfico 4: Distribuição de gastos por tipo de viagem")
    st.markdown("Este gráfico apresenta a distribuição dos gastos com viagens por tipo de viagem (nacional, internacional, etc.) para o cargo selecionado em 2025. \n\n")
