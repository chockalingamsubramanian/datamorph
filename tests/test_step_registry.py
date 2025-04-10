from datamorph.steps.registry import STEP_REGISTRY

def test_registered_step_exists():
    assert "summarize_text" in STEP_REGISTRY
    assert callable(STEP_REGISTRY["summarize_text"])

def test_registered_transform_step():
    assert "transform_data" in STEP_REGISTRY
