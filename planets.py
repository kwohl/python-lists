# Practice: Planet List
planet_list = ["Mercury", "Mars"]
# use append() to add Jupiter and Saturn to the end of the list
planet_list.append("Jupiter")
planet_list.append("Saturn")
# use extend() method to add another list of the lat two planets in our solar system to the end of the list
planet_list.extend(["Uranus", "Neptune"])
# use insert() to add Earth and Venus in the correct order
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
# Use append() again to add Pluto to the end of the list
planet_list.append("Pluto")
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets
rocky_planets = planet_list[:4]
# We know Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list
del planet_list[-1]

# Challenge: Iterating over Planets

spacecrafts = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars"),
    ("Curiosity", "Mars"),
    ("Galileo", "Jupiter"),
    ("New Horizons", "Pluto"),
    ("Voyager 2", "Jupiter", "Saturn", "Neptune", "Uranus"),
    ("MESSENGER", "Mercury"),
    ("Pioneer", "Venus"),
    ("Space Craft", "Saturn")
]

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.


for planet in planet_list:
    planet_crafts = []
    crafts = ""

    for craft_tuple in spacecrafts:
        if planet in craft_tuple:
            planet_crafts.append(craft_tuple[0])

    for planet_craft in planet_crafts:
        if (planet_crafts.index(planet_craft) < (len(planet_crafts)-1)) and len(planet_crafts) > 2:
            crafts = crafts + planet_craft + ', '
        elif (planet_crafts.index(planet_craft) >= len(planet_crafts)-1) and len(planet_crafts) > 2:
            crafts = crafts + 'and ' + planet_craft + '.'
        elif len(planet_crafts) == 1:
            crafts = crafts + planet_craft + '.'
        
    if len(planet_crafts) == 2:
        crafts = planet_crafts[0] + ' and ' + planet_crafts[1] + '.'
    if len(planet_crafts) == 0:
        crafts = "nobody."

    print(f"{planet} was visited by {crafts}")
    # print(f"{planet} was visited by {' and '.join(planet_crafts)}")