from datamorph.core.context_manager import ContextManager

def test_context_manager_store_and_retrieve():
    ctx = ContextManager()
    ctx.update("step1", "result1")
    assert ctx.get("step1") == "result1"

def test_context_manager_snapshot():
    ctx = ContextManager()
    ctx.update("step1", "val1")
    snap = ctx.snapshot()
    assert isinstance(snap, dict)
    assert snap["step1"] == "val1"
