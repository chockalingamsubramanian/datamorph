# Config loader functions (optional)

import yaml
import os

def load_yaml_config(file_name):
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'r') as f:
        return yaml.safe_load(f)
