"""
This module is used for visualizing
the abilities and powers data in the Marvel Universe: Civil War data.
"""
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px  # type: ignore

st.sidebar.success('Select a data visualization to view.')

# Read the data
stats = pd.read_csv('data/charcters_stats.csv')

st.title('Abilities & Powers')
st.markdown('### Plotting from the raw stats data')
st.dataframe(stats)


# Reshape the data
melted_stats = pd.melt(
	stats,
	id_vars=['Alignment', 'Name'],
	var_name='Key',
	value_name='Value',
)
melted_stats = melted_stats[melted_stats['Key'] != 'Total']

# Modify the Alignment column
melted_stats['Alignment'] = melted_stats['Alignment'].str.title()

# Group and arrange the data
grouped_stats = melted_stats.groupby('Key').apply(lambda x: x.sort_values('Value', ascending=False))


# Plotting
fig = px.strip(
	grouped_stats,
	x='Key',
	y='Value',
	color='Key',
	facet_col='Alignment',
	facet_col_wrap=1,
	title='Abilities & Powers',
)

# Update the layout
fig.update_layout(
	legend_title='Abilities & Powers',
	xaxis={'tickfont': {'color': 'white'}},
	yaxis={'tickfont': {}},
	font={'color': 'white'},
)
fig.update_xaxes(title_text='Abilities')
fig.update_yaxes(title_text='Power')

# Display the plot
# fig.show()
st.markdown('### Display the plot')
st.plotly_chart(fig)

# Select and filter the data
filtered_stats = stats.drop(columns=['Name', 'Total']).query('Alignment != ""')

# Reshape the data
melted_stats = pd.melt(filtered_stats, id_vars=['Alignment'], var_name='Key', value_name='Value')

# Drop the rows where Alignment is NaN
melted_stats = melted_stats.dropna(subset=['Alignment'])

# Modify the Alignment column
melted_stats['Alignment'] = melted_stats['Alignment'].str.title()

# Plotting
fig = px.box(
	melted_stats,
	x='Key',
	y='Value',
	color='Alignment',
	facet_col='Alignment',
	facet_col_wrap=1,
	color_discrete_sequence=['#C21E48', '#2C75CB', 'white'],
	title='Alignment & Values',
)

# Update the layout
fig.update_layout(
	plot_bgcolor='black',
	paper_bgcolor='black',
	legend_bgcolor='black',
	legend_title=None,
	xaxis=dict(tickfont=dict(color='cornsilk', size=10)),
	yaxis=dict(tickfont=dict(color='white')),
	legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
	font=dict(color='white'),
	margin=dict(t=50, b=50),
	boxmode='group',
	boxgap=0.3,
	boxgroupgap=0.1,
	showlegend=True,
)

# Set the y-axis limits
fig.update_yaxes(range=[-10, 130])

# Display the plot
st.plotly_chart(fig)

# Create Code Block
CODE_BLOCK = """
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the data
stats = pd.read_csv("data/charcters_stats.csv")

# Reshape the data
melted_stats = pd.melt(
    stats,
    id_vars=["Alignment", "Name"],
    var_name="Key",
    value_name="Value",
)
melted_stats = melted_stats[melted_stats["Key"] != "Total"]

# Modify the Alignment column
melted_stats["Alignment"] = melted_stats["Alignment"].str.title()

# Group and arrange the data
grouped_stats = melted_stats.groupby("Key").apply(lambda x: x.sort_values("Value", ascending=False))

# Plotting
fig = px.strip(
    grouped_stats,
    x="Key",
    y="Value",
    color="Key",
    facet_col="Alignment",
    facet_col_wrap=1,
    title="Abilities & Powers",
)

# Update the layout
fig.update_layout(
    legend_title="Abilities & Powers",
    xaxis={"tickfont": {"color": "white"}},
    yaxis={"tickfont": {}},
    title={"font": {"color": "seagreen"}},
    font={"color": "white"},
)
fig.update_xaxes(title_text="Abilities")
fig.update_yaxes(title_text="Power")

# Display the plot
# fig.show()
st.plotly_chart(fig)
"""

st.code(CODE_BLOCK, language='python')

# Create Code Block
CODE_BLOCK = """
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px  # type: ignore

# Read the data
stats = pd.read_csv('data/charcters_stats.csv')

# Select and filter the data
filtered_stats = stats.drop(columns=['Name', 'Total']).query('Alignment != ""')

# Reshape the data
melted_stats = pd.melt(filtered_stats, id_vars=['Alignment'], var_name='Key', value_name='Value')

# Drop the rows where Alignment is NaN
melted_stats = melted_stats.dropna(subset=['Alignment'])

# Modify the Alignment column
melted_stats['Alignment'] = melted_stats['Alignment'].str.title()

# Plotting
fig = px.box(
	melted_stats,
	x='Key',
	y='Value',
	color='Alignment',
	facet_col='Alignment',
	facet_col_wrap=1,
	color_discrete_sequence=['#C21E48', '#2C75CB', 'white'],
	title='Alignment & Values',
)

# Update the layout
fig.update_layout(
	plot_bgcolor='black',
	paper_bgcolor='black',
	legend_bgcolor='black',
	legend_title=None,
	xaxis=dict(tickfont=dict(color='cornsilk', size=10)),
	yaxis=dict(tickfont=dict(color='white')),
	legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
	font=dict(color='white'),
	margin=dict(t=50, b=50),
	boxmode='group',
	boxgap=0.3,
	boxgroupgap=0.1,
	showlegend=True,
)

# Set the y-axis limits
fig.update_yaxes(range=[-10, 130])

# Display the plot
st.plotly_chart(fig)
"""

st.code(CODE_BLOCK, language='python')

st.markdown('## Tableau Version')

st.image('images/Abilities box.png')
