# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# Functions with multiple inputes
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

# Positional argument
greet_with("Robert", "New York")

# Keyword Argument
greet_with(location="Pennsylvania", name="Joseph")