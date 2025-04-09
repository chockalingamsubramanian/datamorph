# Executes each pipeline step

from datamorph.llm.llm_agent import suggest_next_step
from datamorph.steps.registry import STEP_REGISTRY
from .context_manager import ContextManager

def execute_pipeline(pipeline_steps):
    print("🚀 Starting pipeline execution...\n")

    context = ContextManager()
    context_summary = "No prior steps executed."

    for i, step in enumerate(pipeline_steps, start=1):
        step_name = step.get("step")
        input_data = step.get("input", None)

        print(f"🔹 Step {i}: {step_name}")
        if input_data:
            print(f"  📥 Input: {input_data}")

        # Get and execute the step function
        func = STEP_REGISTRY.get(step_name)
        if func:
            result = func(input_data)
        else:
            print(f"  ⚠️ Step '{step_name}' not implemented. Skipping.\n")
            result = None

        # Update memory/context
        context.update(f"step_{i}_output", result)
        context_summary = str(context.snapshot())

        # Ask LLM what the next step might be
        pipeline_description = f"Current step: {step_name}, Input: {input_data}"
        next_step = suggest_next_step(context_summary, pipeline_description)

        print(f"  🤖 LLM suggests next step could be: **{next_step}**\n")

    print("✅ Pipeline completed.")
