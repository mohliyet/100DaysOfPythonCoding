# Nesting lists in a dictionary
travel_log = {
    "Italy": {"cities_visited": ["Bergamo","Milan","Rome","Napoli"],"total_visits": 4},
    "Germany": {"cities_visited": ["Berlin"],"total_visits": 1},
    "Netherland": {"cities_visited": ["Amsterdam"],"total_visits": 1},
    "Luxembourg": {"cities_visited": ["Luxembourg City"],"total_visits": 1},
}

# Nesting dictionary in a list

travel_log_2 = [
    {
        "Country": "Italy",
        "cities_visited": ["Bergamo","Milan","Rome","Napoli"],
        "total_visits": 4
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin"],
        "total_visits": 1
    },
    {
        "country": "Netherland",
        "cities_visited": ["Amsterdam"],
        "total_visits": 1
    },
    {
        "country": "Luxembourg",
        "cities_visited": ["Luxembourg City"],
        "total_visits": 1
    }
]