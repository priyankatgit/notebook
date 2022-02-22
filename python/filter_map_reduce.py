# def dataset(nr):
#     i = 0
#     while(i<nr):
#         yield i
#         i += 1

# d = dataset(10)
# print([*d])

from functools import reduce

list1 = [*range(10)]

# Filter
odd_nrs = [*filter(lambda x : x%2!=0, list1)]
print(odd_nrs)

#Map
nums = [*map(lambda x : x * x, list1)]
print(nums)

#Reduce
reducer_num = reduce(lambda x,y:x+y, list1)
print(reducer_num)


#Polyfill of filter
def myfilter(func, list):
    result = []
    for l in list:
        if func(l):
            result.append(l)
    return result

even_nrs = [*myfilter(lambda x:x%2==0, list1)]
print(even_nrs)
