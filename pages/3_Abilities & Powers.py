import streamlit as st
import pandas as pd
import plotly.express as px

stats = pd.read_csv('data/charcters_stats.csv')

st.title('Abilities & Powers')
st.markdown('### Plotting from the raw stats data')
st.dataframe(stats)

# Filter the data
# filtered_stats = stats.iloc[-226].query('Alignment != ""')

# Reshape the data
melted_stats = pd.melt(stats, id_vars=['Alignment', 'Name'], var_name='Key', value_name='Value')
melted_stats = melted_stats[melted_stats['Key'] != 'Total']

# st.dataframe(melted_stats)

# Modify the Alignment column
melted_stats['Alignment'] = melted_stats['Alignment'].str.title()

# Group and arrange the data
grouped_stats = melted_stats.groupby('Key').apply(lambda x: x.sort_values('Value', ascending=False))

# st.dataframe(grouped_stats)

# Plotting
fig = px.strip(grouped_stats,
                x='Key',
                y='Value',
                color='Key', 
                facet_col='Alignment',
                facet_col_wrap=1,
                title='Abilities & Powers',)

# Update the layout
fig.update_layout(
    legend_title='Abilities & Powers',
    xaxis=dict(tickfont=dict(color='white')),
    yaxis=dict(tickfont=dict()),
    title=dict(font=dict(color='seagreen',)),
    font=dict(color='white'),
)
fig.update_xaxes(title_text='Abilities')
fig.update_yaxes(title_text='Power')

# Display the plot
# fig.show()
st.plotly_chart(fig)