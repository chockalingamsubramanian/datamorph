import time
from contextlib import contextmanager
from datamorph.utils.logger import get_logger

log = get_logger("DataMorphTimer")

@contextmanager
def timeit(message: str = "Execution time"):
    start = time.time()
    yield
    duration = time.time() - start
    log.info(f"⏱️ {message}: {duration:.2f} seconds")
