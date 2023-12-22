"""
This module is used for visualizing
the demographic data in the Marvel Universe: Civil War data.
"""
import streamlit as st
import pandas as pd

st.markdown("### Plotting from the wiki data")

wiki = pd.read_csv("data/marvel-wikia-data.csv")

# Filter the data
p1 = wiki[wiki["ALIGN"] != ""]
p1["ID"] = p1["ID"].str.replace(" Identity", "")
p1["ID"] = p1["ID"].apply(lambda x: "Null" if x == "" else x)
p1["SEX"] = p1["SEX"].apply(lambda x: "Null" if x == "" else x)
p1["SEX"] = p1["SEX"].str.replace(" Characters", "")
p1["ALIGN"] = p1["ALIGN"].str.replace(" Characters", "")
p1["SEX"] = p1["SEX"].apply(lambda x: "Agender" if x == "Genderfluid" else x)
p1["SEX"] = pd.Categorical(
    p1["SEX"],
    categories=["Male", "Female", "Null", "Agender"],
    ordered=True,
)

st.dataframe(p1)
