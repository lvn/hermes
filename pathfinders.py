import Queue

# helper functions

# check if the tile at the position on the tilemap is passable (an integer)
def position_passable(tilemap, position):
	width = len(tilemap[0])
	height = len(tilemap)
	return position[0] >= 0 and position[1] >= 0 and position[0] < width and position[1] < height and tilemap[position[1]][position[0]]

# get the available neighbors of position
def get_neighbors(tilemap, position):
	(x,y) = position
	return [item for item in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if position_passable(tilemap,item)]

# calculates the Manhattan distance between p1 and p2 (2-tuples)
def manhattan_distance(p1, p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

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
def breadth_first_search(tilemap, start, end):
	height = len(tilemap)
	width = len(tilemap[0])

	frontier = Queue.Queue()
	if position_passable(tilemap, start): 
		frontier.put(start)
		came_from = {start:None}

	while not frontier.empty():
		current = frontier.get()

		# check if current node is the destination
		if current == end: # if so, return path
			return reconstruct_path(came_from, start, end)

		neighbors = get_neighbors(tilemap, current)
		for neighbor in neighbors:
			if neighbor not in came_from:
				frontier.put(neighbor)
				came_from[neighbor] = current
	return []

# dijkstra's algorithm
# like standard BFS, but uses a priority queue instead of a normal queue to find paths by cost
def dijkstra(tilemap, start, end):
	frontier = Queue.PriorityQueue()
	if position_passable(tilemap, start): 
		frontier.put((0,start))
		came_from = {start:None}
		tentative_dist = {start:0}

	while not frontier.empty():
		current = frontier.get()[1]

		# check if current node is the destination
		if current == end: # if so, return path
			return reconstruct_path(came_from, start, end)

		for neighbor in get_neighbors(tilemap, current):
			new_dist = tentative_dist[current] + tilemap[neighbor[1]][neighbor[0]]
			if neighbor not in tentative_dist or tentative_dist[neighbor] > new_dist:
				frontier.put((new_dist, neighbor))
				tentative_dist[neighbor] = new_dist
				came_from[neighbor] = current
	return []

# greedy version of best-first search
# uses heuristic manhattan distance as priority
def greedy_best_first_search(tilemap, start, end):
	frontier = Queue.PriorityQueue()
	if position_passable(tilemap, start): 
		frontier.put((0,start))
		came_from = {start:None}

	while not frontier.empty():
		current = frontier.get()[1]

		# check if current node is the destination
		if current == end: # if so, return path
			return reconstruct_path(came_from, start, end)

		for neighbor in get_neighbors(tilemap, current):
			if neighbor not in came_from:
				heuristic_dist = manhattan_distance(neighbor,end)
				frontier.put((heuristic_dist, neighbor))
				came_from[neighbor] = current
	return []

# A*
# basically combines dijkstra and greedy bfs
def a_star(tilemap, start, end):
	frontier = Queue.PriorityQueue()
	if position_passable(tilemap, start): 
		frontier.put((0,start)) # aka open set
		came_from = {start:None} # doubles as the closed set
		past_dist = {start:0} # aka the past score g(x)

	while not frontier.empty():
		current = frontier.get()[1]

		# check if current node is the destination
		if current == end: # if so, return path
			return reconstruct_path(came_from, start, end)

		for neighbor in get_neighbors(tilemap, current):
			# calculate tentative overall distance
			tentative_past_dist = past_dist[current] + tilemap[neighbor[1]][neighbor[0]]
			if neighbor not in came_from or past_dist[neighbor] > tentative_past_dist:
				# insert into frontier by priority of lower overall_tentative_dist
				heuristic_dist = manhattan_distance(neighbor,end)
				overall_tentative_dist = tentative_past_dist + heuristic_dist

				frontier.put((overall_tentative_dist, neighbor))
				past_dist[neighbor] = tentative_past_dist
				came_from[neighbor] = current
	return []