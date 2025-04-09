# CLI entry point for running a pipeline

import argparse
from .pipeline_loader import load_pipeline
from .executor import execute_pipeline

def main():
    parser = argparse.ArgumentParser(description="Run a DataMorph pipeline.")
    parser.add_argument("config", help="Path to YAML pipeline config")
    args = parser.parse_args()

    pipeline = load_pipeline(args.config)
    execute_pipeline(pipeline)
