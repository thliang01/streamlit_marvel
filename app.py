"""
This module is used for main page for visualizing data related to the Marvel Universe: Civil War.
"""

import streamlit as st

st.sidebar.success('Select a data visualization to view.')

st.title('Marvel Universe: Civil War')

st.markdown('## Marvel Universe Analysis')

st.image('images/hero.gif')

st.markdown('### First Apperances: [Link](https://marvel-viz.streamlit.app/first_appearance)')

st.markdown('#### Demograph: [Link](https://marvel-viz.streamlit.app/demographic)')

st.markdown('### Abilities & Powers: [Link](https://marvel-viz.streamlit.app/abilities_powers)')

st.divider()

st.markdown('## Civil War Analysis: Team Cap vs Team Iron Man')

st.image('images/CapVSIronMan.jpeg')

st.markdown('### Total Power: [Link](https://marvel-viz.streamlit.app/total_power)')
