from traceback import print_exc
from io import StringIO


class LeetCodeTest:
    def __init__(self, _cls, commands, data, _output):
        self._cls = _cls
        self.commands = commands[1:]
        self.data = data[1:]
        self.output = _output[1:]

    def set_str_for_linked_list(self):
        def __str__(self):
            res = ''
            cur = self.left

            while cur:
                res += str(cur.val) + '->' # + ('->' if cur.val != 'r' else '')
                cur = cur.next

            return res

        self._cls.__str__ = __str__

    def run_test(self):
        intance = self._cls()
        for c, d, r in zip(self.commands, self.data, self.output):
            try:
                print(f'before {intance}')
                res = self._cls.__dict__[c](intance, *d)
                print(f'{"success" if res == r else "failed"}. '
                      f'commands: {self._cls.__name__}.{c}({d}), '
                      f'result: {res}, '
                      f'valid result: {r}')
                print(f'after: {intance}')
            except Exception as e:
                buffer = StringIO()
                print_exc(file=buffer)
                print(f'error! '
                      f'commands: {self._cls.__name__}.{c}({d}), '
                      f'valid result: {r}, ')
                print(f'after: {intance}, ')
                print(buffer.getvalue())

            print()
        print('==================' * 10)


def set_null(g):
    g['null'] = None


