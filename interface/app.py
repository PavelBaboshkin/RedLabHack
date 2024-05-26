import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import datetime
from clickhouse_driver import Client


st.set_page_config(layout="wide")
st.title("Прототип команды VZ121")

with st.container():
    col1, col2 = st.columns(2) 

    with col1: 
        st.write("Выбор начала интервала")
        start_date = st.date_input("Дата начала", value=datetime.date(2024, 4, 15), key="s_date")
        start_time = st.time_input('Время начала', value=datetime.time(23, 59), key="s_time")

    with col2: 
        st.write("Выбор окончания интервала")
        end_date = st.date_input("Дата окончания", value=datetime.date(2024, 5, 30), key="e_date")
        end_time = st.time_input('Время окончания', value=datetime.time(23, 59), key="e_time")


start_datetime = datetime.datetime.combine(start_date, start_time)
end_datetime = datetime.datetime.combine(end_date, end_time)
st.write(f"Выбранный период: {start_datetime} - {end_datetime}")


def create_fig(x_ax, y_ax, colors_trace, title):
    trace = go.Scatter(
        x=x_ax, 
        y=y_ax, 
        mode='markers+lines', 
        marker={'color': colors_trace}, 
        line={'color': 'gray'}, 
    )

    return go.Figure(data=trace).update_layout(title=title)


if st.button('Показать графики'):
    query= f"""
            select p.*
                , web_response 
                , throughput
                , apdex
                , error 
            from `default`.probabilities p  
            join `default`.metrices m 
                on p.point = m.point 
            where point between '{start_datetime}' and '{end_datetime}'
            order by point
            """
# '188.120.236.93'
    with Client(host='188.120.236.93') as client:
        df = client.query_dataframe(query)
    
    x = df['point']
    cutoff = 0.5

    if not df.empty:
        col1, col2 = st.columns(2)

        with col1:

            st.plotly_chart(create_fig(x
                                       , df['web_response']
                                       , np.where(df['web_response_proba'] <= cutoff, 'blue', 'red')
                                       , title='web_response'
                                       ))


            st.plotly_chart(create_fig(x
                                       , df['throughput']
                                       , np.where(df['throughput_proba'] <= cutoff, 'blue', 'red')
                                       , title='throughput'
                                       ))
            
        with col2:
            st.plotly_chart(create_fig(x
                                       , df['apdex']
                                       , np.where(df['apdex_proba'] <= cutoff, 'blue', 'red')
                                       , title='apdex'
                                       ))

            st.plotly_chart(create_fig(x
                                       , df['error']
                                       , np.where(df['error_proba'] <= cutoff, 'blue', 'red')
                                       , title='error'
                                       ))
            
    else:
        st.warning('Нет данных для выбранного диапазона.')
else:
    st.write("Для отображения графиков, нажмите кнопку")