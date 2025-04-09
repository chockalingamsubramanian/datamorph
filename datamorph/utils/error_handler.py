# Error catching/decorator

from functools import wraps
from datamorph.utils.logger import get_logger

log = get_logger()

def safe_run(default_return=None):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                log.error(f"Error in {fn.__name__}: {e}")
                return default_return
        return wrapper
    return decorator

