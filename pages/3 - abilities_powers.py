"""
This module is used for visualizing
the abilities and powers data in the Marvel Universe: Civil War data.
"""
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px  # type: ignore

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
	title={'font': {'color': 'seagreen'}},
	font={'color': 'white'},
)
fig.update_xaxes(title_text='Abilities')
fig.update_yaxes(title_text='Power')

# Display the plot
# fig.show()
st.markdown('### Display the plot')
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
