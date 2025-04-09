# (Future) Simulates adaptive context/memory

class ContextManager:
    def __init__(self):
        self.memory = {}

    def update(self, key, value):
        self.memory[key] = value

    def get(self, key, default=None):
        return self.memory.get(key, default)

    def snapshot(self):
        return self.memory.copy()
