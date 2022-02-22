import sys
str1 = "data"
print(id(str1))

str2 = str1
print(id(str2))

print("<<< After modify >>>")
str1 = "data" + "new data"
print(id(str1))
print(id(str2))

print(sys.getrefcount(str1))

# int1 = 0
# print(id(int1))

# int2 = int1
# print(id(int2))

# print("<<< After modify >>>")
# int1 = 10
# print(id(int1))
# print(id(int2))

# print('id of 5 =',id(15))

# a = 5
# print('id of a =',id(a))

# b = a
# print('id of b =',id(b))

# c = 5.0
# print('id of c =',id(c))

# t1 = tuple((1, 2, 3))
# print(id(t1))

# t2 = t1
# print(id(t2))

# print("<<< After modify >>>")
# t1 = t1 * 2
# print(id(t1))
# print(id(t2))


# list1 = [1, 2]
# list2 = list1
# print(id(list1))
# print(id(list2))

# print("<<< After modify >>>")
# list1.append(3)

# print(id(list1))
# print(list2, id(list2))