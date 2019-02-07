my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']


def uncommon_cities(my_cities=my_cities, other_cities=other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    my_set = set(my_cities) ^ set(other_cities)
    return len(my_set)
