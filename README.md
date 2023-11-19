### Flask Project Structure and Server Script Generator

**Objective:**
The script automates the creation of a basic Flask web project structure, including commonly used folders such as 'templates' for HTML templates and 'static' for static files like CSS, JavaScript, and images. Additionally, it generates a `server.py` file with a basic Flask application setup.

**Features:**
1. **Project Structure:**
   - **templates:** Contains HTML templates for your Flask application.
   - **static:**
     - **img:** Folder for storing images.
     - **css:** Folder for CSS files.
     - **js:** Folder for JavaScript files.
   - **server.py:** Flask application setup with a route for the index page and a basic HTML template.

2. **Template Content:**
   - The script generates simple placeholder files within each folder and subfolder.
   - The `server.py` file includes a basic Flask application setup with a route for the index page and a placeholder HTML template.

3. **Usage:**
   - Run the script and provide the desired name for your Flask project when prompted.
   - The script will create the specified project structure and generate a `server.py` file in the current working directory.

**How to Use:**
1. Save the script to your computer.
2. Open a terminal or command prompt.
3. Navigate to the directory where you want to create your Flask project.
4. Run the script (`main.py`).
5. Enter the desired name for your Flask project when prompted.

**Note:**
- Customize the template content in the generated files based on your specific needs after the structure is created.
- The script assumes that you have Python installed on your system.

**Example Output:**
```
Enter the name of your Flask project: my_flask_project
Flask project "my_flask_project" created successfully at /path/to/current/directory/my_flask_project
```

This script provides a starting point for a Flask project, complete with a basic server setup, and allows for further customization as your application requirements evolve.
