

def echo():
    x = None
    while True:
        x = yield x


e = echo()
print(next(e))
print(e.send('hello'))
print(e.send(None))
print(e.send('world'))


def square():
    x = 0
    while True:
        x = yield x
        x = x * x if x is not None else 0


s = square()
print(next(s))
print(s.send(None))
print(s.send(2))
print(s.send(4))
print(s.send(3))

