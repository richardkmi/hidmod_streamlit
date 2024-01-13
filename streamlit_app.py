import pandas as pd
import streamlit as st

df = pd.read_csv("mtcars.csv")

search_term = st.text_input("Search")

if search_term:
    mask = df.apply(lambda row: row.astype(str).str.contains(search_term, regex=False).any(), axis=1)
    df = df[mask]
else:
    df = pd.DataFrame()  # Create an empty dataframe if search term is empty

if search_term == "":
    df = pd.read_csv("mtcars.csv")  # Read the original dataframe if search term is empty

st.table(df)