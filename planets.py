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


