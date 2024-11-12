

class defaultdict(dict):
    def __init__(self, default_factory):
        self.default_factory = default_factory

    def __missing__(self, key):
        self[key] = self.default_factory()
        return self[key]


m = defaultdict(int)
print(m, type(m))
m['a'] += 1

print(m)

