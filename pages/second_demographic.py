"""
This module is used for visualizing
the demographic data in the Marvel Universe: Civil War data.
"""
# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Demographic")
st.markdown("### Plotting from the raw wiki data")

# Read the data
wiki = pd.read_csv("data/marvel-wikia-data.csv")

st.dataframe(wiki)


# Filter the data
p1 = wiki[wiki["ALIGN"] != ""]
p1 = wiki.copy()

# Replace ' Identity' in 'ID' column
p1["ID"] = p1["ID"].str.replace(" Identity", "")

# # Replace empty strings in 'ID' and 'SEX' columns with 'Null'
p1["ID"] = p1["ID"].replace("", "Null")
p1["SEX"] = p1["SEX"].replace("", "Null")

# Remove ' Characters' from 'SEX' and 'ALIGN' columns
p1["SEX"] = p1["SEX"].str.replace(" Characters", "")
p1["ALIGN"] = p1["ALIGN"].str.replace(" Characters", "")

# Replace 'Genderfluid' with 'Agender' in 'SEX' column
p1["SEX"] = p1["SEX"].replace("Genderfluid", "Agender")

# Convert 'SEX' column to categorical and specify the order of categories
p1["SEX"] = pd.Categorical(p1["SEX"], categories=["Male", "Female", "Null", "Agender"], ordered=True)


# st.dataframe(p1)

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.countplot(x="SEX", hue="ALIGN", data=p1, palette=["#C21E48", "#2C75CB", "green"])

# Set the background color to black
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

# Set the labels and title
plt.xlabel(None)
plt.ylabel(None)
plt.title("Alignment / Sex")

# Show the plot
# plt.show()
st.markdown("### PAlignment / Sex Plot")
st.pyplot(plt)

# Prepare the data
# p1_filtered = p1[p1['ID'] != 'Known to Authorities']
p1_filtered = p1.copy()

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.countplot(y="ALIGN", hue="ID", data=p1_filtered, palette=["#C21E48", "#2C75CB", "green", "yellow"])

# Set the background color to black
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

# Move the legend to the top
plt.legend(loc="upper right")

# Set the labels and title
plt.xlabel(None)
plt.ylabel(None)
plt.title("Identity / Alignment")

# Show the plot
# plt.show()
st.markdown("### Identity / Alignment Plot")
st.pyplot(plt)
