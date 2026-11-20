import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

st.title('Первое приложение на Streamlit')

#______________________Текст__________________________

#Заголовки
st.header('Это заголовок')
st.subheader('Это подзаголовок')

#Универсальные функции
st.write('Just some text')

#Пояснительные подписи
st.caption(
    'Пояснительная подпись',
    help='Всплывающая подпись'
    )

st.markdown('# Markdown 1')
st.markdown('## Markdown 2')
st.markdown('### Markdown 3')

st.markdown("""
- level 1
    - level 2
       - level 3

"""
)

st.markdown("<span style='color:red'>Красный текст</span>", unsafe_allow_html=True)


#______________________Табличные данные__________________________

custom_dict = {
    'course' : [1,2,3,4,5],
    'mark' : [8,9,10,6,8]
}


st.write(custom_dict)

custom_df = pd.DataFrame(custom_dict)

st.write(custom_df)

st.header('Это загруженный датасет')

df = pd.read_csv('data/set.csv')
st.write(df)

#______________________ГРАФИКИ__________________________

st.line_chart(
    df.head(70),
    x='Age',
    y='Fare'
)

st.subheader('Barchart')
age_counts = df['Age'].value_counts().sort_index()
st.bar_chart(age_counts, x_label='Возраст', y_label='Количество')


