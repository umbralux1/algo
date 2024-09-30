

def empty_dict(_): return None


def add(d, k, v):
    def new_dict(x):
        if x == k:
            return v
        else:
            return d(x)
    return new_dict


def add_f(d, k, v): return lambda x: v if k == x else d(x)


d = add(empty_dict, "a", 1)

assert d('a') == 1

d = add_f(d, "b", 2)

assert d('a') == 1
assert d('b') == 2
assert d('c') is None
