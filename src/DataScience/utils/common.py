import os
import yaml
from src.DataScience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
        
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' read successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Error converting YAML content to ConfigBox for file: {path_to_yaml}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of directory paths to create.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created or already exists: {path}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The dictionary to save.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully saved to JSON file: {path}")
    except Exception as e:
        raise e
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.
    
    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """
 
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file '{path}' loaded successfully.")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data to a binary file using joblib.

    Args:
        data (Any): The data to save.
        path (Path): The path to the binary file.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data successfully saved to binary file: {path}")
    except Exception as e:
        raise e
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.
        data (Any): The data to load.

    Returns:
        Any: The data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Data successfully loaded from binary file: {path}")
        return data
    except Exception as e:
        raise e