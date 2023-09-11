import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('x')

st.write(x, 'squared is', x*x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    st.table(chart_data)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option