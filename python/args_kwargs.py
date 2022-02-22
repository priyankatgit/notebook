def find_avg(*numbers):
    sum = 0
    for i in numbers :
        sum += i

    print ("average is ",sum/(len(numbers)))
    print (numbers)

find_avg(2,3)
find_avg(2,3,4)
find_avg(1,2,3,4,5,6,7,8,9,10)


def print_values(**values):
	print (values)

print_values(one = 1, two = 2)


# first define a python list variable.
args = [1,2,3,4,5]
find_avg(*args)
# invoke test_arg function and pass above list values. use *args to extract the list values.

x,*y,z = [1,2,3,4,5,6]
print(x)
print(y)
print(z)
