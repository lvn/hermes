# Hermes
### by [Elvin Yung](https://github.com/elvinyung)

"*Know that you shall now be famous among the immortal gods, you and your mother both. These words are true: by my dogwood staff I swear I shall make you the renowned guide of the deathless gods.*"
- [Homeric Hymn to Hermes](http://go.owu.edu/~rlelias/hermes.htm)

## Description
Tilemap pathfinding library in Python. 

## Usage:
`python hermes.py [algorithm] [input_file] [start_x] [start_y] [end_x] [end_y]`

The program will read in the input file as a tilemap, and try to find a path from (`start_x`, `start_y`) to (`end_x`, `end_y`) using the selected algorithm. The program will output a list of points representing the calculated optimal path from (`start_x`, `start_y`) to (`end_x`, `end_y`).

### The Input File
By standard, the program takes as input a plaintext file, where the first line is two numbers delimited by a space, the first representing the width of the grid and the second representing the height. From then on, all other lines are a tilemap representation, where each `1` is an impassible tile, and each `0` is a passable tile. Every character that is not `1` will also be interpreted as `0`. The upper left corner of the map is the origin (0,0), the positive x-direction is to the right, and the positive y-direction is down.

The following is an example of a 6x4 grid:
    000000
    010011
    011010
    001011

### Algorithms
(not all of these are implemented at the moment)
* `bfs` or `breadth-first-search` - [Breadth-first search](http://en.wikipedia.org/wiki/Breadth-first_search).
* `dijkstra` - [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm).
* `greedy-bfs` or `greedy-best-first-search` - Greedy heuristic variant of [best-first search](http://en.wikipedia.org/wiki/Best-first_search).
* `a-star` - the [A* search algorithm](http://en.wikipedia.org/wiki/A*_search_algorithm).