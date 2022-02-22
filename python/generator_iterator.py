# Iterators Python objects that iterate through iterable objects are called Iterators.
nums = [1, 2, 3, 4]
obj = iter(nums)
print(next(obj))


obj = iter("priyank")
print(next(obj))

# Generator
def get_uid():
    i = 0
    while True:
        yield i
        i += 1

# A generator is a type of function that returns a generator object,
uid = get_uid()

# which can return a sequence of values instead of a single result.
print(next(uid))
print(next(uid))
print(next(uid))
print(next(uid))
