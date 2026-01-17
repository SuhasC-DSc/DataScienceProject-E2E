import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="DataScience"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "template/index.html"
]

for filepath in list_of_files:
    path=Path(filepath)

    logging.info(f"Processing file: {path.name} in directory: {path.parent}")

    # Create parent directories if they do not exist
    path.parent.mkdir(parents=True, exist_ok=True)

    # Create the file if it does not exist or is empty
    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"Creating file: {path}")
    else:
        logging.info(f"File already exists: {path}")

# Alternative approach without using pathlib

'''
filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

'''

"""
Why pathlib is better:

* No mixing of os and pathlib
* Cross-platform (Windows, Linux, macOS)
* More readable and modern
* Preferred in production-quality Python code

"""