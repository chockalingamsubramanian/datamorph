from datamorph.core.pipeline_loader import load_pipeline

def test_load_valid_pipeline(tmp_path):
    config_path = tmp_path / "test.yml"
    config_path.write_text("""
    pipeline:
      - step: summarize_text
        input: "data/sample.txt"
    """)
    pipeline = load_pipeline(str(config_path))
    assert isinstance(pipeline, list)
    assert len(pipeline) == 1
    assert pipeline[0]["step"] == "summarize_text"

def test_load_invalid_pipeline(tmp_path):
    config_path = tmp_path / "bad.yml"
    config_path.write_text("invalid_yaml: [")
    try:
        load_pipeline(str(config_path))
        assert False, "Expected failure on invalid YAML"
    except Exception:
        assert True
