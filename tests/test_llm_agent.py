from datamorph.llm.llm_agent import suggest_next_step

def test_suggest_next_step_mock():
    context = "No prior execution"
    description = "Input is raw sales data"
    result = suggest_next_step(context, description)
    assert isinstance(result, str)
    assert result != ""  # Should return something like "transform_data"
