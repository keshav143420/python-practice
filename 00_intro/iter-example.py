class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


r = Reverse([1, 2, 3, 4])
it = iter(r)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("no element left")

print("---------------")
a = list(it)
print(a)
