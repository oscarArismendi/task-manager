import streamlit as st
from persistence.saveTask import save_task 

def reset_fields(): 
    st.session_state["reset_trigger"] = True

def add_task_menu():
    # Initialize session state variables if not set
    if "task_name" not in st.session_state or "reset_trigger" in st.session_state:
        st.session_state["task_name"] = ""
    if "task_status" not in st.session_state or "reset_trigger" in st.session_state:
        st.session_state["task_status"] = "Pending"

    st.session_state.pop("reset_trigger", None)  # Remove the reset trigger

    # Input fields bound to session state
    name = st.text_input("Task Name:", key="task_name")
    status = st.selectbox("Task Status:", ["Pending", "In Progress", "Completed"], key="task_status")


    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save Task"):
            if name.strip():
                save_task(name, status)
                st.success("Task saved successfully!")
            else:
                st.error("Task name cannot be empty.")

    with col2:
        if st.button("Reset Fields"):
            reset_fields()  # Trigger reset fields
            st.rerun()  # Force a re-run to refresh widgets