# CLI entry point for running a pipeline
import argparse
from .pipeline_loader import load_pipeline
from .executor import execute_pipeline
from datamorph.utils.logger import get_logger

log = get_logger("DataMorphRunner")

def main():
    parser = argparse.ArgumentParser(description="Run a DataMorph pipeline.")
    parser.add_argument("config", help="Path to YAML pipeline config")
    args = parser.parse_args()

    log.info(f"📂 Loading pipeline config: {args.config}")
    pipeline = load_pipeline(args.config)
    execute_pipeline(pipeline)
