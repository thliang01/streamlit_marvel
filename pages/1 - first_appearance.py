"""
This module is used for visualizing
the first appearances in the Marvel Universe: Civil War data.
"""

# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.success('Select a data visualization to view.')

st.title('First Apperances')
st.markdown('### Marvel_wiki raw data')

# Read the data
wiki = pd.read_csv('data/marvel-wikia-data.csv')

st.dataframe(wiki)

st.markdown('### Plotting the number of first appearance by year')

# Group by Year and count
chart_data = wiki.groupby('Year').size().reset_index(name='n')

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(chart_data['Year'], chart_data['n'], color='royalblue', alpha=0.8)
ax.plot(chart_data['Year'], chart_data['n'], color='red', linestyle='--')

# Show the plot
st.pyplot(fig)

# Create Code Block
CODE_BLOCK = """
# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
wiki = pd.read_csv("data/marvel-wikia-data.csv")

# Group by Year and count
chart_data = wiki.groupby("Year").size().reset_index(name="n")

# Create the plot
plt.figure(figsize=(10, 6))
plt.fill_between(chart_data["Year"], chart_data["n"], color="royalblue", alpha=0.8)
plt.plot(chart_data["Year"], chart_data["n"], color="red", linestyle="--")
"""

st.code(CODE_BLOCK, language='python')

st.markdown('## Tableau Version')

st.image('images/area and trend chart of _Year of Appearance_.png')
