import streamlit as st
import pandas as pd
import numpy as np

### first iteration
# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)
# st.table(dataframe)

### second iteration
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)
