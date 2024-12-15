import streamlit as st
from persistence.loadAllTasks import load_all_tasks  # Assumed function to load tasks

def list_all_tasks():
    # Constants for pagination
    TASKS_PER_PAGE = 5  

    # Load tasks (Assume this function fetches a list of tasks as dictionaries)
    tasks = load_all_tasks()  # Example: [{"name": "Task 1", "status": "Pending"}, ...]

    if not tasks:
        st.info("No tasks available.")
        return

    # Calculate total pages
    total_pages = -(-len(tasks) // TASKS_PER_PAGE)  # Ceiling division for pages

    # Initialize the session state for pagination if it does not exist
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = 1

    # Display pagination controls
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("Previous", disabled=st.session_state["current_page"] <= 1):
            st.session_state["current_page"] -= 1
            st.rerun()  # Force UI rerender to immediately reflect changes          

    with col3:
        if st.button("Next", disabled=st.session_state["current_page"] >= total_pages):
            st.session_state["current_page"] += 1
            st.rerun()  # Force UI rerender to immediately reflect changes
          

    # Calculate the start and end indices for the current page
    start_idx = (st.session_state["current_page"] - 1) * TASKS_PER_PAGE
    end_idx = start_idx + TASKS_PER_PAGE

    # Display tasks for the current page
    st.subheader(f"Tasks (Page {st.session_state['current_page']} of {total_pages})")
    for i, task in enumerate(tasks[start_idx:end_idx], start=1):
        st.write(f"**{start_idx + i}. {task['name']}** - {task['status']}")

    # Page indicator
    st.text(f"Page {st.session_state['current_page']} of {total_pages}")

    
