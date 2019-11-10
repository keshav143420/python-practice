class FloatRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if round(self.start, 1) >= self.end:
            raise StopIteration
        result = self.start
        self.start += self.step
        return round(result, 1)


#
# r = FloatRange(1.0, 2.0, 0.1)
# it = iter(r)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
print(list(FloatRange(1.0, 2.0, 0.1)))
