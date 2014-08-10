Hermes
=======
by `Elvin Yung <https://github.com/elvinyung>`_

Description
-----------
Tilemap pathfinding library in Python. 

Usage
-----------
Converting a two dimensional block of characters into a tilemap:
::

    from hermes import tilemap
    tile_map_str = '''X1111X1
    1X1XXX1
    111111X
    XXXX111'''
    tile_map = tilemap.str_to_map(tile_map_str)
    # => [[None, 1, 1, 1, 1, None, 1], [1, None, 1, None, None, None, 1], [1, 1, 1, 1, 1, 1, None], [None, None, None, None, 1, 1, 1]]


Pathfinding between two points on a tilemap:
::

    from hermes import pathfinders
    start = (3,0)
    end = (3,6)
    path = pathfinders.a_star(tile_map, start, end)
    # => [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)]

Command-line Demo
-----------------
``python hermes.py [algorithm] [input_file] [start_x] [start_y] [end_x] [end_y]``

The program will read in the input file as a tilemap, and try to find a path from (``start_x``, ``start_y``) to (``end_x``, ``end_y``) using the selected algorithm. The program will output a list of points representing the calculated optimal path from (``start_x``, ``start_y``) to (``end_x``, ``end_y``).

The Input File
-----------------
By standard, the program takes as input a plaintext file, representing a tilemap. Each tile is a number representing the cost to move into that tile, but '0' and 'X' represent impassible tiles. Every character that is not previously mentioned will also be interpreted as ``X``. The upper left corner of the map is the origin (0,0), the positive x-direction is to the right, and the positive y-direction is down.

The following is an example of a 6x4 grid:
::

    111111
    1X1131
    1X2211
    111111


Algorithms
-----------------
- ``bfs`` or ``breadth-first-search`` - `Breadth-first search <http://en.wikipedia.org/wiki/Breadth-first_search>`_.
- ``dijkstra`` - `Dijkstra's algorithm <http://en.wikipedia.org/wiki/Dijkstra's_algorithm>`_.
- ``greedy-bfs`` or ``greedy-best-first-search`` - Greedy heuristic variant of `best-first search <http://en.wikipedia.org/wiki/Best-first_search>`_.
- ``a-star`` - the A* `search algorithm <http://en.wikipedia.org/wiki/A*_search_algorithm>`_.
