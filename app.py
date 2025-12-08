import streamlit as st
import pandas as pd
import joblib
import datetime

model = joblib.load('modelo_atraso_voo.joblib')
scaler = joblib.load('scaler_voo.joblib')

st.title('Previsão de Atrasos em Voos ✈️')

st.header('Insira os Detalhes do Voo para Previsão')

col1, col2 = st.columns(2)

with col1:
    month = st.slider('Mês', 1, 12, 6)
    day = st.slider('Dia do Mês', 1, 31, 15)
    day_of_week = st.slider('Dia da Semana (1=Seg, 7=Dom)', 1, 7, 4)
    airlines = ['AA', 'AS', 'B6', 'DL', 'EV', 'F9', 'HA', 'MQ', 'NK', 'OO', 'UA', 'US', 'VX', 'WN']
    airline_choice = st.selectbox('Companhia Aérea', airlines)

with col2:
    departure_time_obj = st.time_input('Horário de Partida Previsto', value=datetime.time(17, 0))
    arrival_time_obj = st.time_input('Horário de Chegada Previsto', value=datetime.time(19, 0))
    scheduled_time = st.slider('Tempo de Voo Previsto (minutos)', 30, 600, 120)
    distance = st.slider('Distância do Voo (milhas)', 100, 5000, 800)

scheduled_departure = departure_time_obj.hour * 100 + departure_time_obj.minute
scheduled_arrival = arrival_time_obj.hour * 100 + arrival_time_obj.minute

if st.button('Prever Atraso'):
    colunas_modelo = [
        'MONTH', 'DAY', 'DAY_OF_WEEK', 'SCHEDULED_DEPARTURE', 'SCHEDULED_TIME',
        'DISTANCE', 'SCHEDULED_ARRIVAL', 'AIRLINE_AS', 'AIRLINE_B6', 'AIRLINE_DL',
        'AIRLINE_EV', 'AIRLINE_F9', 'AIRLINE_HA', 'AIRLINE_MQ', 'AIRLINE_NK',
        'AIRLINE_OO', 'AIRLINE_UA', 'AIRLINE_US', 'AIRLINE_VX', 'AIRLINE_WN'
    ]

    dados_usuario = {
        'MONTH': month,
        'DAY': day,
        'DAY_OF_WEEK': day_of_week,
        'SCHEDULED_DEPARTURE': scheduled_departure,
        'SCHEDULED_ARRIVAL': scheduled_arrival,
        'SCHEDULED_TIME': scheduled_time,
        'DISTANCE': distance,
    }

    input_df = pd.DataFrame([dados_usuario])
    for col in colunas_modelo:
        if col not in input_df.columns:
            input_df[col] = 0

    if airline_choice != 'AA':
        airline_col = f'AIRLINE_{airline_choice}'
        if airline_col in input_df.columns:
            input_df[airline_col] = 1

    input_df = input_df[colunas_modelo]

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)

    st.subheader('Resultado da Previsão:')
    if prediction[0] == 1:
        st.error(f'ALTO RISCO DE ATRASO 🔴')
        st.write(f"A probabilidade de atraso é de **{prediction_proba[0][1]:.0%}**.")
    else:
        st.success(f'BAIXO RISCO DE ATRASO 🟢')
        st.write(f"A probabilidade de atraso é de apenas **{prediction_proba[0][1]:.0%}**.")