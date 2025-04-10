# Shared loader + executor for UI use
import yaml

def parse_yaml_steps(file_content: str):
    try:
        parsed = yaml.safe_load(file_content)
        return parsed.get("pipeline", [])
    except Exception as e:
        return [{"step": "Invalid YAML", "input": str(e)}]
