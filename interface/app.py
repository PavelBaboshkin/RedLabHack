import streamlit as st

def main():
    st.title("Пример приложения Streamlit")
    st.write("Привет, мир! Это мое первое приложение на Streamlit.")

if __name__ == "__main__":
    main()

# шаблон приложения с локалки

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import datetime

# df = pd.read_csv(r"C:\Users\pbabo\Downloads\precalculated.csv"
#                  , header=None
#                  , names=['point', 'web_response', 'throughput', 'apdex', 'error'])
# df['point'] = pd.to_datetime(df['point'])


# st.set_page_config(layout="wide")
# st.title("Прототип команды VZ121")


# with st.container():
#     col1, col2 = st.columns(2) 

#     with col1: 
#         st.write("Выбор начала интервала")
#         start_date = st.date_input("Дата начала", value=datetime.date(2024, 4, 15), key="s_date")
#         start_time = st.time_input('Время начала', value=datetime.time(23, 59), key="s_time")

#     with col2: 
#         st.write("Выбор окончания интервала")
#         end_date = st.date_input("Дата окончания", value=datetime.date(2024, 5, 30), key="e_date")
#         end_time = st.time_input('Время окончания', value=datetime.time(23, 59), key="e_time")


# start_datetime = datetime.datetime.combine(start_date, start_time)
# end_datetime = datetime.datetime.combine(end_date, end_time)
# st.write(f"Выбранный период: {start_datetime} - {end_datetime}")


# if st.button('Показать графики'):
#     filtered_data = df.sort_values(by='point')#[(df['point'] >= start_datetime) & (df['point'] <= end_datetime)]

#     if not filtered_data.empty:
#         col1, col2 = st.columns(2)

#         with col1:
#             fig1 = px.line(filtered_data, x='point', y='web_response', title='Web Response Time')
#             st.plotly_chart(fig1)

#             fig3 = px.line(filtered_data, x='point', y='apdex', title='Apdex Score')
#             st.plotly_chart(fig3)
            
#         with col2:
#             fig2 = px.line(filtered_data, x='point', y='throughput', title='Throughput')
#             st.plotly_chart(fig2)

#             fig4 = px.line(filtered_data, x='point', y='error', title='Error Rate')
#             st.plotly_chart(fig4)
            
#     else:
#         st.warning('Нет данных для выбранного диапазона.')
# else:
#     st.write("Пожалуйста, нажмите кнопку для отображения графиков.")