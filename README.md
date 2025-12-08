# ✈️ Análise e Previsão de Atrasos em Voos

## 🚀 Acesse o Aplicativo Interativo

O modelo foi publicado em uma aplicação web com Streamlit. Você pode acessá-la e testá-la através do link abaixo:

## https://previsao-atrasos-voos.streamlit.app/


---


## 📄 Descrição do Projeto

Este projeto consiste em um pipeline de Machine Learning de ponta a ponta que prevê a probabilidade de atrasos em voos comerciais nos EUA. O processo incluiu desde a análise exploratória de um grande volume de dados até o deploy de um modelo preditivo em uma aplicação web interativa com Streamlit.

## 🛠️ Ferramentas Utilizadas

*   **Análise e Modelagem:** Python, Pandas, NumPy, Scikit-learn, Joblib, Jupyter Notebook
*   **Aplicação Web:** Streamlit
*   **Deploy:** Streamlit Community Cloud

## 📈 Análise e Resultados do Modelo

O modelo de Regressão Logística foi treinado para identificar voos com mais de 15 minutos de atraso. A avaliação demonstrou a capacidade do modelo de identificar corretamente **60% (Recall)** de todos os voos que realmente atrasaram.

Para um problema de aviação, priorizar o **Recall** é fundamental, pois o custo de um atraso não previsto é muito maior do que o de um "alarme falso".

## 🚀 Como Executar Localmente

1.  **Clone o repositório:**
    ```
    git clone https://github.com/MaykonAragao/previsao-atrasos-voos.git
    ```
2.  **Navegue até a pasta do projeto:**
    ```
    cd previsao-atrasos-voos
    ```
3.  **Instale as dependências:**
    ```
    pip install -r requirements.txt
    ```
4.  **Execute o aplicativo Streamlit:**
    ```
    streamlit run app.py
    ```

---

A análise exploratória completa e o processo de treinamento do modelo podem ser encontrados no notebook `analise_atrasos_voos.ipynb`.
