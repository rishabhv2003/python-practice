t = (1, 2, 3, 4)
tu = 'rihsabh'
print(type(tu))  # Output: <class 'str'>

tu = ('rishabh',)  # Correct way to create a tuple with a single element
print(type(tu))    # Output: <class 'tuple'>

# Check if 'rishabh' exists in the tuple before trying to find its index
if 'rishabh' in tu:
    print(tu.index('rishabh'))  # Output: 0
else:
    print("'rishabh' not found in the tuple")

# Define a tuple
my_tuple = ('apple', 'banana', 'cherry', 'banana')

# Find the index of the first occurrence of 'banana' in the tuple
index = my_tuple.index('banana')

print("Index of 'banana':", index)  # Output: Index of 'banana': 1