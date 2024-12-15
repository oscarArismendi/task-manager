from persistence.connection import get_db_session
from models.taskEntity import Task

def update_task(task_id, new_name, new_status):
    # Update an existing task in the database.
    session = get_db_session()
    try:
        # Fetch the task by ID
        task = session.query(Task).filter_by(id=task_id).first()
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")

        # Update the task fields
        task.name = new_name
        task.status = new_status

        session.commit()  # Commit the changes
        print(f"Task '{task_id}' updated successfully!")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Error updating task: {e}")
        raise e
    finally:
        session.close()
