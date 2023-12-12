import streamlit as st
import pandas as pd

st.title('Marvel Universe: Civil War')

st.markdown('## Marvel_characters_info raw data')

info = pd.read_csv('data/marvel_characters_info.csv')

st.dataframe(info)
