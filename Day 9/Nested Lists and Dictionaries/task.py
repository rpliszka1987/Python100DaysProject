# Dictionary Nested
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

# Nested List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

# Nested Dictionary in dictionary
travel_log_new = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"],
    },
}

print(travel_log_new["Germany"]["cities_visited"][0])