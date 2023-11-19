import os

def create_flask_project(project_name):
    project_structure = {
        'templates': ['index.html'],
        'static': {
            'img': [],
            'css': [],
            'js': []
        },
        'server.py': [
            'from flask import Flask, render_template\n\n',
            f'app = Flask(__name__, template_folder="templates")\n\n',
            f'@app.route("/")\n',
            f'def index():\n',
            f'    return render_template("index.html")\n\n',
            f'if __name__ == "__main__":\n',
            f'    app.run(host="0.0.0.0", port=80, debug=True)'
        ]
    }

    project_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_path)

    for folder, contents in project_structure.items():
        if folder.endswith('.py'):
            file_path = os.path.join(project_path, folder)
            with open(file_path, 'w') as file:
                file.writelines(contents)
        else:
            folder_path = os.path.join(project_path, folder)
            os.makedirs(folder_path)

            for content in contents:
                content_path = os.path.join(folder_path, content)
                if content.endswith('.html') or content.endswith('.css') or content.endswith('.js'):
                    with open(content_path, 'w') as file:
                        file.write(f'<!-- {content} file for {project_name} -->')

    print(f'Flask project "{project_name}" created successfully at {project_path}')

if __name__ == '__main__':
    project_name = input('Name of your Flask project -> ')
    create_flask_project(project_name)
