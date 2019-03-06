import doctest
from character import get_pokemon


def pokemon_map():
    """Interpret a square map with user location and available spots.

    PRECONDITION character must be a well-formed dictionary seen in get_pokemon
    >>> pokemon_map({"Name": "Dave", "Class": "Bulbasaur", "Position": [2, 3], "HP": 10})
    X X X X
    X X X X
    X X X X
    X X P X
    >>> pokemon_map({"Name": "Fred", "Class": "Charmander", "Position": [0, 0], "HP": 8})
    P X X X
    X X X X
    X X X X
    X X X X
    >>> pokemon_map({"Name": "Henry", "Class": "Squirtle", "Position": [3, 3], "HP": 3})
    X X X X
    X X X X
    X X X X
    X X X P
    """
    map_positions = [["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "X", "X", "X"]]

    pokemon_x = get_pokemon()["Position"][0]
    pokemon_y = get_pokemon()["Position"][1]
    map_positions[pokemon_y][pokemon_x] = "P"

    for row in map_positions:
        print(" ".join(row))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
