import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
import pandas as pd
data = pd.read_csv("data.csv",sep=";")
# Create columns

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
# col5, col6 = st.columns(2)
# col7, col8 = st.columns(2)
# col9, col10 = st.columns(2)
# col11, col12 = st.columns(2)
# col13, col14 = st.columns(2)
# col15, col16 = st.columns(2)
# col17, col18 = st.columns(2)
with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Welcome To Franco's Journey Through programming!")
    content = """
        Cool Programmer with a lot fo skills in python and javascript as well as Java. 
    """
    st.write(content)


# with col3:
#     st.title(data.iloc[2]['title'])
#     st.image(f"images/{data.iloc[2]['image']}")
#     st.info(data.iloc[2]['description'])
#
# with col4:
#     st.title(data.iloc[3]['title'])
#     st.image(f"images/{data.iloc[3]['image']}")
#     st.info(data.iloc[3]['description'])

with col3:
    for idx, row in data[10:].iterrows():
        st.title(row['title'])
        st.image(f"images/{row['image']}")
        st.write(row['description'])

with col4:
    for idx, row in data[:10].iterrows():
        st.title(row['title'])
        st.image(f"images/{row['image']}")
        st.write(row['description'])