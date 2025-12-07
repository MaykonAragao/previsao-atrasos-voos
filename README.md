# ✈️ Análise e Previsão de Atrasos em Voos

![Status](https://img.shields.io/badge/status-Parte%201%20Conclu%C3%ADda-blue)

## 📄 Descrição do Projeto

Este projeto tem como objetivo construir um pipeline de Machine Learning de ponta a ponta para prever atrasos em voos comerciais. Ele é dividido em duas partes:

*   **Parte 1 (Concluída):** Análise Exploratória de Dados (EDA), limpeza, engenharia de features e treinamento de um modelo de classificação (Regressão Logística).
*   **Parte 2 (Em andamento):** Desenvolvimento de uma aplicação web interativa com Streamlit para consumir o modelo treinado e fazer previsões em tempo real.

## 🛠️ Ferramentas Utilizadas

*   **Linguagem:** Python 3
*   **Bibliotecas:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib
*   **Ambiente:** Jupyter Notebook

## 📈 Resultados do Modelo (Parte 1)

O modelo de Regressão Logística foi treinado para identificar voos com mais de 15 minutos de atraso. A avaliação demonstrou a capacidade do modelo de identificar corretamente **60% (Recall)** de todos os voos que realmente atrasaram, provando ser uma ferramenta útil para alertar a equipe de operações.

A análise completa, o código de treinamento e os artefatos do modelo (`.joblib`) estão neste repositório.

## 🚀 Como Executar a Análise

1.  **Baixe o Dataset:** O dataset (`flights.csv`) é muito grande para ser incluído neste repositório. Faça o download diretamente do Kaggle através deste [link](https://www.kaggle.com/datasets/usdot/flight-delays?select=flights.csv).
2.  **Estrutura de Pastas:** Crie uma pasta `data` na raiz do projeto e coloque o `flights.csv` dentro dela.
3.  **Execute o Notebook:** Abra o arquivo `analise_atrasos_voos.ipynb` em um ambiente Jupyter e execute as células.
