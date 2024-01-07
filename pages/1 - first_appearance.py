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

# Group by 'Year' and count the number of appearances
year_counts = wiki['Year'].value_counts().sort_index()

# Create an area chart
plt.figure(figsize=(10, 6))
plt.fill_between(year_counts.index, year_counts, color='skyblue', alpha=0.4)
plt.plot(year_counts.index, year_counts, color='Slateblue', alpha=0.6)

plt.title('Number of First Appearances by Year')
plt.xlabel('Year')
plt.ylabel('Number of First Appearances')

# Display the plot in Streamlit
st.markdown('### Plotting the number of first appearance by year')
st.pyplot(plt)

# Create Code Block
CODE_BLOCK = """
# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
wiki = pd.read_csv("data/marvel-wikia-data.csv")

# Group by 'Year' and count the number of appearances
year_counts = wiki['Year'].value_counts().sort_index()

# Create an area chart
plt.figure(figsize=(10,6))
plt.fill_between(year_counts.index, year_counts, color="skyblue", alpha=0.4)
plt.plot(year_counts.index, year_counts, color="Slateblue", alpha=0.6)

plt.title('Number of First Appearances by Year')
plt.xlabel('Year')
plt.ylabel('Number of First Appearances')

# Display the plot in Streamlit
st.pyplot(plt)
"""

st.code(CODE_BLOCK, language='python')

st.markdown('## Tableau Version')

st.image('images/area and trend chart of _First Appearance_.png')
