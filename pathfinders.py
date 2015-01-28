import Queue, graph

# heuristic functions

# calculates the Manhattan distance between p1 and p2 (2-tuples)

# manhattan: grid distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# euclidean: straight-line distance between two points
def euclidean_distance(p1, p2):
    return (abs(p1[0]-p2[0])**2.0 + abs(p1[1]-p2[1])**2.0)**0.5

# zero: no heuristic
def zero_heuristic(p1, p2):
    return 0.0

heuristic_fns = {
    'manhattan': manhattan_distance,
    'euclidean': euclidean_distance,
    'none': zero_heuristic,
    'default': manhattan_distance
}

# helper functions

# check if the tile at the position on the graph is passable (an integer)
def position_passable(graph, position):
    width = len(graph[0])
    height = len(graph)
    return position[0] >= 0 and position[1] >= 0 and position[0] < width and position[1] < height and graph[position[1]][position[0]]

# get the available neighbors of position
def get_neighbors(graph, position):
    (x,y) = position
    return [item for item in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if position_passable(graph,item)]

# reconstructs path from a came_from dict, a startpoint, and an endpoint
def reconstruct_path(came_from, start, end):
    path = []
    current = end
    while current != start:
        #print current
        path.insert(0,current)
        current = came_from[current]
    else:
        path.insert(0,start)
    return path

# standard BFS from startpoint to endpoint. 
def breadth_first_search(graph, start, end):
    frontier = Queue.Queue()
    if position_passable(graph, start): 
        frontier.put(start)
        came_from = {start:None}
    else:
        raise Exception("invalid starting position")

    while not frontier.empty():
        current = frontier.get()

        # check if current node is the destination
        if current == end: # if so, return path
            return reconstruct_path(came_from, start, end)

        neighbors = get_neighbors(graph, current)
        for neighbor in neighbors:
            if neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = current
    return []

# dijkstra's algorithm
# like standard BFS, but uses a priority queue instead of a normal queue to find paths by cost
def dijkstra(graph, start, end):
    frontier = Queue.PriorityQueue()
    if position_passable(graph, start): 
        frontier.put((0,start))
        came_from = {start:None}
        tentative_dist = {start:0}
    else:
        raise Exception("invalid starting position")

    if not position_passable(graph, end):
        raise Exception("invalid end position")

    while not frontier.empty():
        current = frontier.get()[1]

        # check if current node is the destination
        if current == end: # if so, return path
            return reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(graph, current):
            new_dist = tentative_dist[current] + graph[neighbor[1]][neighbor[0]]
            if neighbor not in tentative_dist or tentative_dist[neighbor] > new_dist:
                frontier.put((new_dist, neighbor))
                tentative_dist[neighbor] = new_dist
                came_from[neighbor] = current
    return []

# greedy version of best-first search
# uses heuristic manhattan distance as priority
def greedy_best_first_search(graph, start, end, heuristic='default'):
    if heuristic not in heuristic_fns:
        heuristic = 'default'
    heuristic = heuristic_fns[heuristic]

    frontier = Queue.PriorityQueue()
    if position_passable(graph, start): 
        frontier.put((0,start))
        came_from = {start:None}
    else:
        raise Exception("invalid starting position")

    if not position_passable(graph, end):
        raise Exception("invalid end position")

    while not frontier.empty():
        current = frontier.get()[1]

        # check if current node is the destination
        if current == end: # if so, return path
            return reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(graph, current):
            if neighbor not in came_from:
                heuristic_dist = heuristic(neighbor,end)
                frontier.put((heuristic_dist, neighbor))
                came_from[neighbor] = current
    return []

# A*
# basically combines dijkstra and greedy bfs
def a_star(graph, start, end, heuristic='default'):
    if heuristic not in heuristic_fns:
        heuristic = 'default'
    heuristic = heuristic_fns[heuristic]

    frontier = Queue.PriorityQueue()
    if position_passable(graph, start): 
        frontier.put((0,start)) # aka open set
        came_from = {start:None} # doubles as the closed set
        past_dist = {start:0} # aka the past score g(x)
    else:
        raise Exception("invalid starting position")

    if not position_passable(graph, end):
        raise Exception("invalid end position")

    while not frontier.empty():
        current = frontier.get()[1]

        # check if current node is the destination
        if current == end: # if so, return path
            return reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(graph, current):
            # calculate tentative overall distance
            tentative_past_dist = past_dist[current] + graph[neighbor[1]][neighbor[0]]
            if neighbor not in came_from or past_dist[neighbor] > tentative_past_dist:
                # insert into frontier by priority of lower overall_tentative_dist
                heuristic_dist = heuristic(neighbor,end)
                overall_tentative_dist = tentative_past_dist + heuristic_dist

                frontier.put((overall_tentative_dist, neighbor))
                past_dist[neighbor] = tentative_past_dist
                came_from[neighbor] = current
    return []