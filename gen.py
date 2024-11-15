

def echo():
    x = None
    while True:
        x = yield x


e = echo()
print(next(e))
print(e.send('hello'))
print(e.send(None))
print(e.send('world'))
