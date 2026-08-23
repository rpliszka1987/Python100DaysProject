# Dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Adding to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Empty Dictionary
empty_dictionary = {}

# Wipe existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in dictionary
programming_dictionary["Loop"] = "This is a new value"
print(programming_dictionary)

# Loop through dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

