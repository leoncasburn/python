planets = {"Mars": {"moons": 2, "distance_from_sun_km": 227900000, "length_of_day_hours": 25}, 
           "Jupiter": {"moons": 95, "distance_from_sun_km": 778500000, "length_of_day_hours": 10}, 
           "Saturn": {"moons": 146, "distance_from_sun_km": 1434000000, "length_of_day_hours": 11},
           "Uranus": {"moons": 28, "distance_from_sun_km": 2900000000, "length_of_day_hours": 17},
           "Neptune": {"moons": 16, "distance_from_sun_km": 4500000000, "length_of_day_hours": 16},
           "Venus": {"moons": 0, "distance_from_sun_km": 108000000, "length_of_day_hours": 5832},
           "Mercury": {"moons": 0, "distance_from_sun_km": 58000000, "length_of_day_hours": 1408},
           "Earth": {"moons": 1, "distance_from_sun_km": 150000000, "length_of_day_hours": 24},
}

while True:
    chosen_planet = input("Enter a planet name: (or 'quit' to exit)").capitalize()
    if chosen_planet == "Quit":
        break
    if chosen_planet in planets:
        print(f"{chosen_planet} has {planets[chosen_planet]['moons']} "
              f"moons and is {planets[chosen_planet]['distance_from_sun_km']}kms from the Sun. "
              f"It's day lasts {planets[chosen_planet]['length_of_day_hours']} hours")
    else:
        print("That planet does not exist")
