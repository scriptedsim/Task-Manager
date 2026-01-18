import streamlit as st
from functions import get_todos, write_todos

st.title("My todo app")
st.text_input(label="", placeholder="Add new todo . . .")

todos = get_todos()
for todo in todos:
    st.checkbox(todo)

