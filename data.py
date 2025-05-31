import os

project_structure = {
    "lib": {
        "cli.py": "",
        "helpers.py": "",
        "debug.py": "",
        "db": {
            "__init__.py": "",
            "models.py": "",
            "seed.py": ""
        }
    },
    "README.md": "",
    "Pipfile": "",
    "Pipfile.lock": ""
}

base_path = "/mnt/data/restaurant_reservation"

def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

create_project_structure(base_path, project_structure)
base_path
