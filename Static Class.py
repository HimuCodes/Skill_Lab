# Class definition for MyClass
class MyClass:
    """A class with instance and static methods."""

    def __init__(self, x):
        """Initializes the MyClass instance with an attribute x."""
        self.x = x

    def display(self):
        """Prints the value of the attribute x for the instance."""
        print("The value of x is:", self.x)

    @staticmethod
    def static_method():
        """Prints a message indicating this is a static method."""
        print("This is a static method")

# Creating an object of MyClass
obj = MyClass(5)

# Accessing the instance method display()
obj.display()

# Accessing the static method without creating an object
MyClass.static_method()

