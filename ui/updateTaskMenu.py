import streamlit as st
from persistence.loadAllTasks import load_all_tasks
from persistence.updateTask import update_task  

def update_task_menu():
    # Search functionality
    st.header("Update Task")
    search_term = st.text_input("Search for a task by name", key="search_term")

    # Load tasks and filter by search term
    tasks = load_all_tasks()
    filtered_tasks = [task for task in tasks if search_term.lower() in task["name"].lower()]

    if not filtered_tasks and search_term:
        st.info(f"No tasks found containing '{search_term}'.")
        return

    # Show filtered tasks
    if filtered_tasks:
        task_names = [task["name"] for task in filtered_tasks]
        selected_task_name = st.selectbox("Select a task to update", task_names, key="selected_task")

        # Find the selected task details
        selected_task = next(task for task in filtered_tasks if task["name"] == selected_task_name)

        # Editable fields
        updated_name = st.text_input("Task Name", value=selected_task["name"], key="updated_name")
        updated_status = st.selectbox(
            "Task Status", options=["Pending", "In Progress", "Completed"], index=["Pending", "In Progress", "Completed"].index(selected_task["status"]), key="updated_status"
        )

        # Save button
        if st.button("Save Changes"):
            # Call persistence layer to update task
            try:
                if updated_name.strip():
                    update_task(selected_task["id"], updated_name, updated_status)
                    st.success(f"Task '{updated_name}' updated successfully!")
                else:
                    st.error("Task name cannot be empty.")
            except Exception as e:
                st.error(f"Failed to update task: {e}")
