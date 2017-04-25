import datetime
from functools import wraps

class Timeit:
    def __init__(self, fn = None):
            wraps(fn)(self)
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self.__wrapped__(*args, **kwargs)
        cost = datetime.datetime.now() - start
        print(cost)
        return ret

    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self, *args):
        cost = datetime.datetime.now() - self.start
        print(cost)

if __name__ == "__main__":
    with Timeit() as it:
        z = 3 + 8
        print(z)

    @Timeit
    def add(x, y):
        return x+y
    print(add(2,3))
