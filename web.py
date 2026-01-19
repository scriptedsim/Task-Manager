import streamlit as st
from functions import get_todos, write_todos

st.title("My todo app")

def add_todos():
    # Fetch the value from session state
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    write_todos(todos)


st.text_input(label="Add a todo", 
              label_visibility="collapsed",
              placeholder="Add new todo . . .", 
              key="new_todo", 
              on_change=add_todos)

todos = get_todos()
for todo in todos:
    st.checkbox(todo)

print("Script execution finished (hello)")
st.session_state