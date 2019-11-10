def float_range(start, end, step):
    while start < end:
        result = start
        yield round(result, 1)
        start += step


#
# it = iter(float_range(1.0, 2.0, 0.1))
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

print(list(float_range(1.0, 2.9, 0.1)))
