# Loads and parses YAML pipeline definitions

import yaml

def load_pipeline(path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    
    pipeline = config.get("pipeline", [])
    if not pipeline:
        raise ValueError("No steps found in the pipeline config.")
    
    return pipeline
