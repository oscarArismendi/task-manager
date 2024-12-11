# Task Manager
## **Setting Up MySQL Database Locally**

To run this project, you need a local MySQL database. Follow these steps to set it up:

### **Step 1: Install MySQL**
1. Download and install MySQL Community Server from the [official MySQL website](https://dev.mysql.com/downloads/mysql/).
2. During installation, note the username (`root` by default) and set a password for the MySQL server.

---

### **Step 2: Open MySQL**
1. Open a terminal (Command Prompt or PowerShell on Windows).
2. Access MySQL by running:
   ```
   mysql -u root -p
   ```
   Replace `root` with your username if it's different. Enter your password when prompted.

---

### **Step 3: Create the Database**
1. Once inside the MySQL shell, create a database by running:
   ```
   CREATE DATABASE taskManager;
   ```
2. Verify the database was created by running:
   ```
   SHOW DATABASES;
   ```

---

### **Step 4: Construct Your Database URL**
Your SQLAlchemy connection URL should follow this format:
```
mysql+pymysql://your_username:your_password@localhost:3306/taskManager
```

- Replace `your_username` with your MySQL username.
- Replace `your_password` with your MySQL password.

For example:
```
mysql+pymysql://root:example_password@localhost:3306/taskManager
```

---

### **Step 5: Update the `.env` File**
Create a `.env` file in the project root directory and add the following:
``` 
DB_URL=mysql+pymysql://your_username:your_password@localhost:3306/taskManager
```

Replace the placeholders with your actual MySQL credentials.

---


Now your MySQL database is ready to use with this project!

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
