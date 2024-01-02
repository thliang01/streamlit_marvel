import pandas as pd
import plotly.express as px
import streamlit as st

st.sidebar.success('Select a data visualization to view.')

st.title('comparison')

# Read the data
stats = pd.read_csv('data/charcters_stats.csv')

# Display the raw data
st.markdown('### Display the raw data')
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

# Create a new DataFrame for the VS matchups
vs_matchups = pd.DataFrame(
	{
		'Name': [
			'Black Panther',
			'Iron Man',
			'Black Widow',
			'Vision',
			'Spider-Man',
			'War Machine',
			'Winter Soldier',
			'Captain America',
			'Scarlet Witch',
			'Hawkeye',
			'Ant-Man',
			'Falcon',
		],
		'VS': [
			'Winter Soldier vs Black Panther',
			'Iron Man vs Captain America',
			'Black Widow vs Scarlet Witch',
			'Vision vs Hawkeye',
			'Spider-Man vs Ant-Man',
			'War Machine vs Falcon',
			'Winter Soldier vs Black Panther',
			'Iron Man vs Captain America',
			'Black Widow vs Scarlet Witch',
			'Vision vs Hawkeye',
			'Spider-Man vs Ant-Man',
			'War Machine vs Falcon',
		],
	}
)

# Merge the VS matchups DataFrame with the filtered_stats DataFrame
merged_stats = pd.merge(filtered_stats, vs_matchups, on='Name')

# Reshape the data
melted_stats = pd.melt(
	merged_stats, id_vars=['Name', 'Team', 'VS'], var_name='Key', value_name='Value'
)

# Filter for Black Panther and Winter Soldier
filtered_melted_stats = melted_stats[melted_stats['Name'].isin(['Black Panther', 'Winter Soldier'])]

# Plotting
fig = px.bar(
	melted_stats,
	x='VS',
	y='Value',
	color='Name',
	facet_row='Key',
	labels={'Value': 'Value', 'VS': 'VS'},
	color_discrete_sequence=[
		'#9D152C',
		'#080808',
		'#7A1F1E',
		'#1849CA',
		'#a71930',
		'#6f195f',
		'#AA0505',
		'#FF3D3D',
		'#DF1F2D',
		'#00991f',
		'#666666',
		'#9a9a9a',
	],
)

# Update the layout
fig.update_layout(
	plot_bgcolor='#F6F6F7',
	paper_bgcolor='#F6F6F7',
	title={
		'text': 'Team Iron Man vs Team Cap',
		'x': 0.5,
		'y': 0.95,
		'xanchor': 'center',
		'yanchor': 'top',
	},
	font=dict(color='#0E305D', size=20),
	showlegend=False,
)

# Display the plot
st.markdown('### Display the plot')
# st.plotly_chart(fig)
st.image('images/analysis.png')

# Display the code block
CODE_BLOCK = """
import pandas as pd
import plotly.express as px
import streamlit as st

st.title('comparison')

# Read the data
stats = pd.read_csv('data/charcters_stats.csv')

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

# Create a new DataFrame for the VS matchups
vs_matchups = pd.DataFrame(
	{
		'Name': [
			'Black Panther',
			'Iron Man',
			'Black Widow',
			'Vision',
			'Spider-Man',
			'War Machine',
			'Winter Soldier',
			'Captain America',
			'Scarlet Witch',
			'Hawkeye',
			'Ant-Man',
			'Falcon',
		],
		'VS': [
			'Winter Soldier vs Black Panther',
			'Iron Man vs Captain America',
			'Black Widow vs Scarlet Witch',
			'Vision vs Hawkeye',
			'Spider-Man vs Ant-Man',
			'War Machine vs Falcon',
			'Winter Soldier vs Black Panther',
			'Iron Man vs Captain America',
			'Black Widow vs Scarlet Witch',
			'Vision vs Hawkeye',
			'Spider-Man vs Ant-Man',
			'War Machine vs Falcon',
		],
	}
)

# Merge the VS matchups DataFrame with the filtered_stats DataFrame
merged_stats = pd.merge(filtered_stats, vs_matchups, on='Name')

# Reshape the data
melted_stats = pd.melt(
	merged_stats, id_vars=['Name', 'Team', 'VS'], var_name='Key', value_name='Value'
)

# Filter for Black Panther and Winter Soldier
filtered_melted_stats = melted_stats[melted_stats['Name'].isin(['Black Panther', 'Winter Soldier'])]

# Plotting
fig = px.bar(
	melted_stats,
	x='VS',
	y='Value',
	color='Name',
	facet_row='Key',
	labels={'Value': 'Value', 'VS': 'VS'},
	color_discrete_sequence=[
		'#9D152C',
		'#080808',
		'#7A1F1E',
		'#1849CA',
		'#a71930',
		'#6f195f',
		'#AA0505',
		'#FF3D3D',
		'#DF1F2D',
		'#00991f',
		'#666666',
		'#9a9a9a',
	],
)

# Update the layout
fig.update_layout(
	plot_bgcolor='#F6F6F7',
	paper_bgcolor='#F6F6F7',
	title={
		'text': 'Team Iron Man vs Team Cap',
		'x': 0.5,
		'y': 0.95,
		'xanchor': 'center',
		'yanchor': 'top',
	},
	font=dict(color='#0E305D', size=20),
	showlegend=False,
)

# Display the plot
st.plotly_chart(fig)
"""

# Display the code block
st.code(CODE_BLOCK)

st.markdown('## Tableau Version')

st.image('images/Black Widow vs. Scarlet Witch.png')
