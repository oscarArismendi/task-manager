from persistence.connection import get_db_session
from models.taskEntity import Task

def save_task(name, status):
    """Save a new task to the database."""
    session = get_db_session()
    try:
        # Create a new Task object
        task = Task(name=name, status=status)
        session.add(task)  # Add to session
        session.commit()  # Commit the transaction
        print(f"Task '{name}' with status '{status}' saved successfully!")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Error saving task: {e}")
    finally:
        session.close()