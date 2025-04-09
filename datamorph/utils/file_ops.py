# Reusable file utilities (read/write/check)

import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def file_exists(path):
    return os.path.isfile(path)

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

