import streamlit as st

from ui.addTaskMenu import add_task_menu
from ui.listAllTaskMenu import list_all_tasks
from ui.updateTaskMenu import update_task_menu
from ui.deleteTaskMenu import delete_task_menu
from ui.saveAndLoadTaskMenu import save_and_load_task_menu

def main_menu():
    st.title("Task Manager")
    option = st.selectbox(
        "Choose an option:",
        [
            "Add Task",
            "List All Tasks",
            "Update Task Status",
            "Delete Task",
            "Save and Load Tasks"
        ]
    )

    if option == "Add Task":
        add_task_menu()
    elif option == "List All Tasks":
        list_all_tasks()
    elif option == "Update Task Status":
        update_task_menu()
    elif option == "Delete Task":
        delete_task_menu()
    elif option == "Save and Load Tasks":
        save_and_load_task_menu()
