import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Marvel Universe: Civil War')

st.markdown('## Marvel Universe Analysis')
st.markdown('### Marvel_wiki raw data')

wiki = pd.read_csv('data/marvel-wikia-data.csv')

st.dataframe(wiki)

st.markdown('### Plotting the number of first appearance by year')
# Group by Year and count
chart_data = wiki.groupby('Year').size().reset_index(name='n')

# Create the plot
plt.figure(figsize=(10, 6))
plt.fill_between(chart_data['Year'], 
                 chart_data['n'], 
                 color='royalblue', 
                 alpha=0.8)
plt.plot(chart_data['Year'], chart_data['n'], 
         color='red', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Number of First Appearance')
plt.title('Marvel Universe: Civil War')
plt.grid(True, linewidth=0.1, color='gray')
plt.xticks(color='gray', size=12)
plt.yticks(color='gray', size=12)
plt.ylim(0, max(chart_data['n']) + 10)

st.pyplot(plt)
