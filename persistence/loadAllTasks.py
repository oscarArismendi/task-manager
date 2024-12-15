from persistence.connection import get_db_session
from models.taskEntity import Task

def load_all_tasks():
    # Load all tasks from the database
    session = get_db_session()
    try:
        # Query all tasks from the database
        tasks = session.query(Task).all()  
        
        # Convert Task objects into dictionaries for easy use in the UI
        task_list = [{"name": task.name, "status": task.status} for task in tasks]
        return task_list
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
    finally:
        session.close()
