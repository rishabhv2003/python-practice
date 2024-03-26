class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialization code
        self.value = "This is a singleton instance"

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

# Creating instances of the Singleton class
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()

# Both instances should refer to the same object
print(singleton1 == singleton2)  # Output: True

# Accessing attributes of the singleton instance
print(singleton1.value)  # Output: This is a singleton instance
print(singleton2.value)  # Output: This is a singleton instance
