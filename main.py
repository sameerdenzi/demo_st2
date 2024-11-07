import streamlit as st
import pandas as pd
import numpy as np

st.link_button("Profile",url="/1_profile")

data = pd.read_csv("Task.csv")
st.write(data) 

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.write(chart_data)
st.bar_chart(chart_data)
st.line_chart(chart_data)
