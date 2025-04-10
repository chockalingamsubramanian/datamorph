# Executes each pipeline step

from datamorph.llm.llm_agent import suggest_next_step
from datamorph.steps.registry import STEP_REGISTRY
from datamorph.core.context_manager import ContextManager
from datamorph.utils.logger import get_logger
from datamorph.utils.timer import timeit

log = get_logger("DataMorphExecutor")

def execute_pipeline(pipeline_steps):
    log.info("🚀 Starting pipeline execution...")

    context = ContextManager()
    context_summary = "No prior steps executed."

    for i, step in enumerate(pipeline_steps, start=1):
        step_name = step.get("step")
        input_data = step.get("input", None)

        log.info(f"🔹 Step {i}: {step_name}")
        if input_data:
            log.info(f"📥 Input: {input_data}")

        func = STEP_REGISTRY.get(step_name)
        if func:
            with timeit(f"Execution time for step '{step_name}'"):
                result = func(input_data)
        else:
            log.warning(f"⚠️ Step '{step_name}' not implemented. Skipping.")
            result = None

        context.update(f"step_{i}_output", result)
        context_summary = str(context.snapshot())

        pipeline_description = f"Current step: {step_name}, Input: {input_data}"
        next_step = suggest_next_step(context_summary, pipeline_description)

        log.info(f"🤖 LLM suggests next step: **{next_step}**\n")

    log.info("✅ Pipeline completed.")
