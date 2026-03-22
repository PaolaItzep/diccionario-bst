class Association:
    def __init__(self, key, value):
        self.key = key.lower()
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return f"({self.key}, {self.value})"