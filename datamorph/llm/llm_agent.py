# Core LLM interface to generate decisions or step suggestions

from datamorph.llm.openai_connector import call_llm # <-- Use this during Prod
# from datamorph.llm.mock_connector import call_llm  # <-- Use this during development

from datamorph.llm.prompts import STEP_DECISION_PROMPT_TEMPLATE

def suggest_next_step(context_summary, pipeline_description):
    prompt = STEP_DECISION_PROMPT_TEMPLATE.format(
        context=context_summary,
        description=pipeline_description
    )
    response = call_llm(prompt)
    return response.strip()
