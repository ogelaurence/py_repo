import streamlit as st

st.sidebar.header(" This is a simple calculator ")
x = st.number_input( " Choose first no : ")
y = st.number_input(" Choose second no : ")

col1,col2 = st.columns(2)
with col1 :
    if st.button(" Add"):
        z = x + y
        st.write( f''' Answer is \n
                    {z} ''')
with col2:
    if st.button(" Sub "):
        z = x- y
        st.write(f''' Answer is \n
                    {z} ''')
