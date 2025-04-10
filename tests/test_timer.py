from datamorph.utils.timer import timeit

def test_timeit_runs():
    called = False
    with timeit("test"):
        called = True
    assert called
