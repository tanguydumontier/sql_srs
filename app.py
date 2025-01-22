import streamlit as st
import pandas as pd
import duckdb

st.write("Hello, World!")
data = {
    "a": [1, 2, 3, 4],
    "b": [10, 20, 30, 40]
}

df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    sql_query = st.text_area(label="Entrez votre query ici")
    result = duckdb.query(sql_query)
    st.write(f"Vous avez entré la query suivante : {sql_query}")
    st.dataframe(result)