# Prepare list without comprehension
even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

# List using comprehension
even_numbers = [i for i in range(10) if i % 2 == 0] 
print(even_numbers)

list_of_tuples = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list_of_tuples)


# Prepare dictionary without comprehension
even_numbers = {}
for i in range(10):
    even_numbers[i] = "Even" if i % 2 == 0 else "Odd"

print(even_numbers)

# Prepare dictionary with comprehension
even_numbers = { i: "Even" if i % 2 == 0 else "Odd" for i in range(10) }

print(even_numbers)

# Prepare tuple using comprehension
even_numbers = set((i for i in range(10) if i % 2 == 0))
print(even_numbers)

# Prepare generator using comprehension
even_numbers = (i for i in range(10) if i % 2 == 0)
for even in even_numbers:
    print(even)

# Prepare tuple using comprehension
even_numbers = tuple((i for i in range(10) if i % 2 == 0))
print(even_numbers)