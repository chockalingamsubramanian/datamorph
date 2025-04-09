# Registers all available steps
from .summarize import summarize_text
from .transform import transform_data

STEP_REGISTRY = {
    "summarize_text": summarize_text,
    "transform_data": transform_data,
}
