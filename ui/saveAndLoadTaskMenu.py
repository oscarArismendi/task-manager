import streamlit as st
import json

from persistence.saveLoadTasks import export_tasks_to_json, import_tasks_from_json
from utils.jsonHelpers import load_json

def save_and_load_task_menu():
    # UI for saving and loading tasks via JSON files.
    st.title("Save and Load Tasks")
    st.write("Manage tasks with JSON files: Save tasks to a JSON file or load tasks from a JSON file.")

    # Preview the current database
    if st.button("Preview Current Database"):
        try:
            export_tasks_to_json()
            with open("data/tasks.json", "r") as f:
                tasks_json = f.read()
            st.json(tasks_json)
        except Exception as e:
            st.error(f"Failed to load tasks: {e}")

    # Save tasks to JSON
    st.subheader("Save Tasks to JSON")
    if st.button("Download Tasks JSON"):
        try:
            json_file_path = export_tasks_to_json()
            with open(json_file_path, "r") as f:
                st.download_button("File ready to download(Press again)", f, file_name="tasks.json")
        except Exception as e:
            st.error(f"Failed to export tasks: {e}")

    # Load tasks from JSON
    st.subheader("Load Tasks from JSON")
    uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
    if uploaded_file:
        try:
            # Convert UploadedFile to a string and write to a temporary file
            temp_file_path = "data/temp_uploaded.json"
            with open(temp_file_path, "w") as temp_file:
                temp_file.write(uploaded_file.getvalue().decode("utf-8"))  # Decode the file content
            
            # Load the JSON from the temporary file
            parsed_json = load_json(temp_file_path)
            
            # Preview the uploaded JSON
            st.write("### Uploaded JSON Preview")
            st.json(parsed_json)

            if st.button("Load Tasks from JSON"):
                try:
                    import_tasks_from_json(temp_file_path)
                    st.success("Tasks successfully loaded from the uploaded JSON!")
                except Exception as e:
                    st.error(f"Error loading tasks: {e}")
        except Exception as e:
            st.error(f"Invalid JSON file: {e}")
