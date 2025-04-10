# Registers all available steps
from datamorph.steps.summarize import summarize_text
from datamorph.steps.transform import transform_data
from datamorph.steps.s3_loader import load_data_from_s3
from datamorph.steps.dynamo_writer import write_to_dynamo

STEP_REGISTRY = {
    "summarize_text": summarize_text,
    "transform_data": transform_data,
    "load_data_from_s3": load_data_from_s3,
    "write_to_dynamo": write_to_dynamo,
}