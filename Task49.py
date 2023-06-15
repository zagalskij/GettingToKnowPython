def find_farthest_orbit(list_of_orbits): 
    squares = dict()
    for x in list_of_orbits:
        if x[0] != x[1]:
            squares[3.14 * x[0] * x[1]] = list_of_orbits.index(x)
    return list_of_orbits[squares[max(squares)]]


orbits = [(6, 6), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
