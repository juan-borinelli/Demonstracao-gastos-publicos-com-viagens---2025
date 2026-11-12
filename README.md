# 📊 Gastos Públicos com Viagens — 2025

Análise exploratória dos dados de viagens a serviço de servidores públicos federais em 2025, extraídos do [Portal da Transparência do Governo Federal](https://portaldatransparencia.gov.br/download-de-dados/viagens). Os dados são tratados com **Pandas** e apresentados em um painel interativo feito com **Streamlit**.

O objetivo é identificar padrões de gasto, os cargos que mais viajam e possíveis anomalias nos dados. O projeto também serve como exercício prático de manipulação de um volume grande de dados reais.

## Destaques da análise

Alguns números da tabela consolidada (`output/tabela_final_2025.csv`):

- Mais de **300 mil viagens** aparecem sem o cargo do servidor informado (agrupadas como `NAO IDENTIFICADO`), somando cerca de **R$ 1,15 bilhão**.
- Cerca de **114 mil viagens**, que somam aproximadamente **R$ 429 milhões**, estão marcadas como *Informações protegidas por sigilo*.
- Entre os cargos identificados, **Professor do Magistério Superior** é o que mais viaja: quase 55 mil viagens e cerca de R$ 122 milhões.
- **Técnico do Seguro Social** tem a maior despesa média por viagem (cerca de R$ 5 mil) e a maior duração média (mais de 12 dias).
- **Brasília/DF** é o destino mais frequente para quase todos os cargos.

## Funcionalidades

- **Página inicial:** apresentação do projeto, tabela consolidada completa e atalhos para o Portal da Transparência e para o repositório.
- **Dashboard:** filtro por cargo na barra lateral e seleção do indicador a ser exibido (número de viagens, gastos totais, gasto médio por viagem e distribuição por tipo de viagem).
- **Relatório final:** página reservada para as conclusões da análise.

> 🚧 Projeto em desenvolvimento: os gráficos do dashboard e o relatório final ainda estão sendo implementados.

## Como funciona

O processamento fica no notebook `analise.ipynb`, que:

1. Lê o arquivo bruto `input/2025_Viagem.csv` (separador `;`, codificação `latin1`).
2. Converte os valores monetários (diárias, passagens, devoluções e outros gastos) para número.
3. Cria a coluna **Valor total**, que soma diárias, passagens e outros gastos.
4. Preenche os cargos ausentes com `NAO IDENTIFICADO`.
5. Converte as datas e calcula o mês e a duração de cada viagem, em dias.
6. Agrupa os dados por cargo, calculando:
   - despesa média;
   - duração média;
   - despesa total;
   - destino mais frequente;
   - número de viagens.
7. Mantém só os cargos com **mais de 1% do total de viagens**.
8. Exporta o resultado para `output/tabela_final_2025.csv`, que é a tabela lida pelo painel.

### Colunas da tabela final

| Coluna | Descrição |
|---|---|
| `Cargo` | Cargo do servidor |
| `despesa_media` | Gasto médio por viagem (R$) |
| `duracao_media` | Duração média das viagens (dias) |
| `despesas_totais` | Soma dos gastos com viagens (R$) |
| `destinos_mais_frequentes` | Destino mais comum entre as viagens do cargo |
| `n_viagens` | Quantidade de viagens |

## Tecnologias

- Python 3.11
- [Pandas](https://pandas.pydata.org/), para tratamento e agregação dos dados
- [Streamlit](https://streamlit.io/), para o painel interativo
- [uv](https://docs.astral.sh/uv/), para gerenciar o ambiente e as dependências
- Jupyter Notebook, para a análise

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/juan-borinelli/Demonstracao-gastos-publicos-com-viagens---2025.git
cd Demonstracao-gastos-publicos-com-viagens---2025
```

### 2. Instale as dependências

Com o [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Ou com o pip:

```bash
pip install streamlit pandas openpyxl
```

### 3. Rode o painel

```bash
uv run streamlit run "1_🏠_home.py"
```

Se não estiver usando o uv, rode `streamlit run "1_🏠_home.py"`.

O painel abre no navegador, em `http://localhost:8501`. A tabela consolidada já vem no repositório, então não é preciso baixar os dados brutos para usar o painel.

### (Opcional) Refazer a análise com os dados brutos

O arquivo bruto é grande demais para ficar no repositório e está no `.gitignore`. Para gerar a tabela de novo:

1. Baixe os dados de **Viagens 2025** no [Portal da Transparência](https://portaldatransparencia.gov.br/download-de-dados/viagens).
2. Extraia o arquivo `2025_Viagem.csv` para uma pasta `input/` na raiz do projeto.
3. Execute o notebook `analise.ipynb`. Ele vai gravar uma nova versão de `output/tabela_final_2025.csv`.

> Para analisar outro ano, mude a variável `ano_analise` no início do notebook e baixe o arquivo do ano correspondente.

## Estrutura do projeto

```
├── 1_🏠_home.py                  # página inicial do painel
├── pages/
│   ├── 2_📈_dashboard.py         # dashboard com filtro por cargo
│   └── 3_📝_relatorio_final.py   # relatório final
├── analise.ipynb                 # tratamento e consolidação dos dados
├── output/
│   └── tabela_final_2025.csv     # tabela consolidada usada pelo painel
├── pyproject.toml                # dependências do projeto
└── uv.lock
```

## Fonte dos dados

Os dados vêm do **Portal da Transparência do Governo Federal**, mantido pela Controladoria-Geral da União (CGU), e são públicos.

## Autor

Desenvolvido por [Juan Borinelli](https://github.com/juan-borinelli).
