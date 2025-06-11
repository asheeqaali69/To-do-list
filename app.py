import streamlit as st

st.title("📅 To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "new_task" not in st.session_state:
    st.session_state.new_task = ""


def add_task():
    task = st.session_state.new_task.strip()
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = "" 


st.text_input("Add a task:", key="new_task", on_change=add_task)


if st.button("Add"):
    add_task()

for i, task in enumerate(st.session_state.tasks):
    if st.checkbox(task, key=i):
        st.session_state.tasks.pop(i)
        st.rerun()
