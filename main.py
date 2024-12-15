import os

from models.taskEntity import Task,Base
from persistence.connection import init_db, get_db_session, engine
from utils.jsonHelpers import load_json,save_json, file_path_generator
from ui.mainMenu import main_menu

from sqlalchemy.orm import sessionmaker



script_directory = os.path.dirname(os.path.abspath(__file__))
file_path_tasks = file_path_generator(script_directory,"data","tasks.json") # Initial path Json campers

# Defining main function
def main():

    # Initialize the database (only needs to be run once)
    init_db(Base)
    
    # Create a session
    session = get_db_session()


    t1 = Task("Connect with JSON", "ONGOING")
    print(t1)
    print("Testing load:")
    loadJson = load_json(file_path_tasks)
    print(loadJson)
    print("adding a task")
    loadJson.append(t1.to_dict())
    print(loadJson)
    print("Saving json file")
    save_json(loadJson,file_path_tasks)
    secondLoadJson = load_json(file_path_tasks)
    print(secondLoadJson)


if __name__=="__main__":
    main_menu()