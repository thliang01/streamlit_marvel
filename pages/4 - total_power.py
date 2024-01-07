import pandas as pd
import plotly.express as px
import streamlit as st

st.sidebar.success('Select a data visualization to view.')

st.title('Total Power')

# Read the data
stats = pd.read_csv('data/charcters_stats.csv')

# Display the raw data
st.markdown('### Display the raw data')

# Show the raw data
st.write(stats)

# Mutate the Team column
stats['Team'] = stats['Name'].map(
	{
		'Black Panther': 'Team Iron Man',
		'Iron Man': 'Team Iron Man',
		'Black Widow': 'Team Iron Man',
		'Vision': 'Team Iron Man',
		'Spider-Man': 'Team Iron Man',
		'War Machine': 'Team Iron Man',
		'Winter Soldier': 'Team Cap',
		'Captain America': 'Team Cap',
		'Scarlet Witch': 'Team Cap',
		'Hawkeye': 'Team Cap',
		'Ant-Man': 'Team Cap',
		'Falcon': 'Team Cap',
	}
)

# Filter out rows with missing Team values
filtered_stats = stats.dropna(subset=['Team'])

# Reshape the data
melted_stats = pd.melt(filtered_stats, id_vars=['Name', 'Team'], var_name='Key', value_name='Value')

# Filter for Key == "Total"
filtered_stats = melted_stats[melted_stats['Key'] == 'Total']

# Plotting
fig = px.bar(
	filtered_stats,
	x='Value',
	y='Name',
	color='Team',
	orientation='h',
	color_discrete_sequence=['#1849CA', '#AA0505'],
	labels={'Value': 'Total', 'Name': 'Name'},
	title='Total Power of the Team by Characters',
)

# Update the layout
fig.update_layout(
	plot_bgcolor='black',
	paper_bgcolor='black',
	legend_bgcolor='black',
	legend_title=None,
	xaxis=dict(tickfont=dict(color='white', size=10)),
	yaxis=dict(tickfont=dict(color='white')),
	font=dict(color='white'),
	margin=dict(t=50, b=50),
	showlegend=False,
)

# Display the plot
st.markdown('### Display the plot')

# Display the plot
st.plotly_chart(fig)

# Create Code Block
CODE_BLOCK = """
import pandas as pd
import plotly.express as px
import streamlit as st

# Read the data
stats = pd.read_csv('data/charcters_stats.csv')

# Mutate the Team column
stats['Team'] = stats['Name'].map({
    "Black Panther": "Team Iron Man",
    "Iron Man": "Team Iron Man",
    "Black Widow": "Team Iron Man",
    "Vision": "Team Iron Man",
    "Spider-Man": "Team Iron Man",
    "War Machine": "Team Iron Man",
    "Winter Soldier": "Team Cap",
    "Captain America": "Team Cap",
    "Scarlet Witch": "Team Cap",
    "Hawkeye": "Team Cap",
    "Ant-Man": "Team Cap",
    "Falcon": "Team Cap"
})

# Filter out rows with missing Team values
filtered_stats = stats.dropna(subset=['Team'])

# Reshape the data
melted_stats = pd.melt(filtered_stats, id_vars=['Name', 'Team'], var_name='Key', value_name='Value')

# Filter for Key == "Total"
filtered_stats = melted_stats[melted_stats['Key'] == 'Total']

# Plotting
fig = px.bar(
    filtered_stats,
    x='Value',
    y='Name',
    color='Team',
    orientation='h',
    color_discrete_sequence=["#1849CA", "#AA0505"],
    labels={'Value': 'Total', 'Name': 'Name'},
    title='Total Power of the Team by Characters'
)

# Update the layout
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    legend_bgcolor='black',
    legend_title=None,
    xaxis=dict(tickfont=dict(color='white', size=10)),
    yaxis=dict(tickfont=dict(color='white')),
    font=dict(color='white'),
    margin=dict(t=50, b=50),
    showlegend=False
)

# Display the plot
st.plotly_chart(fig)
"""

st.code(CODE_BLOCK)

st.markdown('## Tableau Version')

st.image('images/Dashboard for Total power of the team by characters.png')
