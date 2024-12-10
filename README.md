# Task Manager

## Installation and Setup Guide (Windows)

### 1. Set Up a Virtual Environment

To start, you'll need to create a virtual environment for the project. This helps isolate the project's dependencies from your system's Python installation.

- Open your terminal (Command Prompt or PowerShell).
- Navigate to your project directory:
  ```
  cd path\to\task_manager
  ```

### 2. Create a Virtual Environment

Next, create a new virtual environment with the following command:
  ```
  python -m venv venv
  ``` 
This will create a folder named `venv` inside your project directory, where all the project dependencies will be stored.

### 3. Activate the Virtual Environment

Activate the virtual environment to begin using it:
  ```
  venv\Scripts\activate
  ``` 
Once activated, your terminal prompt will change to show `(venv)`, indicating that the virtual environment is now active.

### 4. Install Project Dependencies

With the virtual environment active, install the required dependencies listed in the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ``` 
This will automatically install all the necessary libraries for your project.

### 5. Verify Installation

To ensure that the dependencies have been installed correctly, you can check the list of installed packages with:
  ```
  pip list
  ``` 
This should display all the libraries and their respective versions that are installed in the virtual environment.

### 6. Run Your Project

You are now ready to run your project. Execute the main Python script with the following command:
  ```
  python main.py
  ```

### 7. Deactivate the Virtual Environment

Once you are done working with the project, deactivate the virtual environment:
  ```
  deactivate
  ``` 
This will return your terminal session to the global Python environment.

---

By following these steps, you'll ensure that your project is set up correctly with all the necessary dependencies installed, isolated in a virtual environment for easy management.
