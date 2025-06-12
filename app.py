import streamlit as st

st.title("📅 To-Do List")

st.session_state.setdefault("tasks", [])

with st.form("task_form", clear_on_submit=True):
    new_task = st.text_input("Add a task:")
    submitted = st.form_submit_button("Add")
    if submitted and new_task.strip():
        st.session_state.tasks.append(new_task.strip())

for i, task in enumerate(st.session_state.tasks):
    if st.checkbox(task, key=f"task_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()
