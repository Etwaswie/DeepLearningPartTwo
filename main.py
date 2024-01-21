import streamlit as st
import pandas as pd


st.title('Введите ид работника [0: 9923], в ответ выведем 3 наиболее подходящие вакансии')
st.subheader('С работниками и вакансиями можно ознакомиться в датасетах test_recs.csv и vacancies.csv соответственно')

matching = pd.read_csv('./data/matching_id_vacs.csv')
id = st.number_input("Введите ид работника", value=0, min_value=0, max_value=9923, step=1)
finding = matching[matching['id'] == id]['Ищет работу на должность:'][id]

v1 = matching[matching['id'] == id]['vac1'][id]
v2 = matching[matching['id'] == id]['vac2'][id]
v3 = matching[matching['id'] == id]['vac3'][id]

st.text('Введенный ид ищет работу на должность:	' + finding)
st.text('Рекомендуем следующие вакансии:')
st.text('1 - ' + v1)
st.text('2 - ' + v2)
st.text('3 - ' + v3)