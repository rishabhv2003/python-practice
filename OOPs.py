class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing instance attributes using self
print(my_car.display_info())  # Output: Make: Toyota, Model: Camry


print()
print("*"*20)
print()

class MyClass:
    def __init__(self):
        self.public_attr = 10
        self._protected_attr = 20
        self.__private_attr = 30

    def public_method(self):
        return "This is a public method"

    def _protected_method(self):
        return "This is a protected method"

    def __private_method(self):
        return "This is a private method"


obj = MyClass()

# Accessing public attributes and methods
print(obj.public_attr)  # Output: 10
print(obj.public_method())  # Output: This is a public method

# Accessing protected attributes and methods
print(obj._protected_attr)  # Output: 20
print(obj._protected_method())  # Output: This is a protected method

# Attempting to access private attributes and methods (will result in an error)
# print(obj.__private_attr)  # Raises AttributeError
# print(obj.__private_method())  # Raises AttributeError

# Accessing private attributes and methods (name mangling)
print(obj._MyClass__private_attr)  # Output: 30
print(obj._MyClass__private_method())  # Output: This is a private method
