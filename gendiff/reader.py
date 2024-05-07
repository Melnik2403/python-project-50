import yaml
import json
import fnmatch


def read(file_path: str):
    if fnmatch.fnmatch(file_path, '*.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    elif fnmatch.fnmatch(file_path, '*.json'):
        file = json.load(open(file_path))
        return file
