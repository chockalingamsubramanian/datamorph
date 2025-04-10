from datamorph.llm.llm_agent import suggest_next_step

def test_suggest_next_step_mock():
    context = "Previously ran summarize_text"
    description = "Input is a customer feedback document"
    result = suggest_next_step(context, description)
    assert isinstance(result, str)
    assert result != ""
