import os

from persistence.loadAllTasks import load_all_tasks
from persistence.deleteTask import delete_all_tasks
from persistence.saveTask import save_task
from utils.jsonHelpers import save_json, load_json, file_path_generator,default_json

TASKS_FILE_PATH = file_path_generator(os.getcwd(), "data", "tasks.json")

def export_tasks_to_json():
    # Export all tasks from the database to a JSON file.
    default_json()
    tasks = load_all_tasks()
    save_json(tasks, TASKS_FILE_PATH)
    return TASKS_FILE_PATH

def import_tasks_from_json(file_path):
    """
    Replace all tasks in the database with tasks from a JSON file.
    The JSON file can contain tasks without IDs.
    """
    data = load_json(file_path)
    if not isinstance(data, list):
        raise ValueError("Invalid format: The JSON file should contain a list of tasks.")
    
    # Clear the database
    delete_all_tasks()

    # Add tasks to the database
    for task in data:
        save_task(task['name'],task['status']) 
