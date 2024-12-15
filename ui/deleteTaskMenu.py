import streamlit as st
from persistence.loadAllTasks import load_all_tasks
from persistence.deleteTask import delete_task
from time import sleep

def delete_task_menu():
    """UI for deleting a task."""
    st.title("Delete Task")
    st.write("Search for a task by name and delete it.")

    # Input for filtering tasks by name
    search_term = st.text_input("Search for a task by name")
    
    # Load all tasks
    tasks = load_all_tasks()

    # Filter tasks based on the search term
    filtered_tasks = [task for task in tasks if search_term.lower() in task["name"].lower()]
    
    # Show filtered tasks for selection
    if filtered_tasks:
        selected_task_name = st.selectbox(
            "Select a task to delete",
            options=[task["name"] for task in filtered_tasks],
            key="selected_task_name",
        )

        # Get the selected task details
        selected_task = next(task for task in filtered_tasks if task["name"] == selected_task_name)
        task_id = selected_task["id"]

        # Show task details
        st.write("### Task Details")
        st.write(f"**Name:** {selected_task['name']}")
        st.write(f"**Status:** {selected_task['status']}")

        # Delete button with confirmation
        if st.button("Delete Task", key="delete_task_button"):
            try:
                delete_task(task_id)  # Call the persistence layer to delete
                st.success(f"Task '{selected_task['name']}' deleted successfully!")
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Failed to delete task: {e}")

    else:
        st.info("No tasks match your search.")
