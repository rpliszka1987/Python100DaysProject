# Functions with return
def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"

formated_string = format_name("robert", "pLiszka" )
print(formated_string)

#Passing return value to another string
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))
print(output)

