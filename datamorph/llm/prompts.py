# Stores reusable prompt templates
# Prompt templates used for LLM interaction

STEP_DECISION_PROMPT_TEMPLATE = """
You are a smart pipeline decision engine.
Given the following context and pipeline description, decide what the next best step should be.

Context:
{context}

Pipeline Description:
{description}

Reply with the name of the next step only.
"""
