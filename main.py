import streamlit as st
import pandas as pd

st.title('Введите ид работника [0: 19], в ответ выведем 3 наиболее подходящие вакансии')
st.subheader('С работниками и вакансиями можно ознакомиться в датасетах test_recs.csv и vacancies.csv соответственно')

uid_to_vname = pd.read_csv('./data/uid_to_vname.csv')
number = st.number_input("Введите ид работника", value=0, min_value = 0, max_value=19, step=1)
vacs_to_u = uid_to_vname[uid_to_vname['id'] == number]['v_names'][number]
st.text(vacs_to_u)