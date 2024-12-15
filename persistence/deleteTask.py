from persistence.connection import get_db_session
from models.taskEntity import Task

def delete_task(task_id):
    # Delete a task from the database
    session = get_db_session()
    try:
        # Query the task by ID
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)  # Delete the task
            session.commit()  # Commit the transaction
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            raise ValueError(f"No task found with ID {task_id}.")
    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print(f"Error deleting task: {e}")
        raise e
    finally:
        session.close()