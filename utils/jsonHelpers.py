import json,os

# # #functions about json
def save_json(database,file_path):
    try:
      with open(file_path, 'w') as archivo_json:
        json.dump(database, archivo_json, indent=2)
        
    except FileNotFoundError:
        print("The JSON doesn't exist")
    except json.JSONDecodeError:
        print("The format of the archive is not JSON")
    except Exception as e:
        print("Unknow error")
        
def load_json(file_path):
    try:
      with open(file_path, 'r') as archivo_json:        
        data = json.load(archivo_json)
        return data
    except Exception as e:
      print(f"Error to load: {e}")

def file_path_generator(original_path,directory_name,json_name):
    data_directory = os.path.join(original_path, directory_name)
    if not os.path.exists(data_directory):# Create the "data" directory if it doesn't exist
        os.makedirs(data_directory)
    rta = os.path.join(data_directory, json_name)
    return rta

def default_json(database = "[]" , file_path = file_path_generator(os.getcwd(), "data", "tasks.json")):
    try:
      with open(file_path, 'w') as archivo_json:
        json.dump(database, archivo_json, indent=2)
        
    except FileNotFoundError:
        print("The JSON doesn't exist")
    except json.JSONDecodeError:
        print("The format of the archive is not JSON")
    except Exception as e:
        print("Unknow error")