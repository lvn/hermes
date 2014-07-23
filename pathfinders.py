import Queue

def position_passable(tilemap, position):
	width = len(tilemap[0])
	height = len(tilemap)
	return position[0] >= 0 and position[1] >= 0 and position[0] < width and position[1] < height \
		and isinstance(tilemap[position[1]][position[0]], int)

# get the available neighbors of position
def get_neighbors(tilemap, position):
	(x,y) = position
	return [item for item in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if position_passable(tilemap,item)]

# standard BFS from startpoint to endpoint. 
def breadth_first_search(tilemap, start, end):
	height = len(tilemap)
	width = len(tilemap[0])

	frontier = Queue.Queue()
	if position_passable(tilemap, start): frontier.put(start)
	came_from = {start:None}

	while not frontier.empty():
		current = frontier.get()

		# check if current node is the destination
		if current == end: # if so, return path
			path = []
			while current != start:
				#print current
				path.insert(0,current)
				current = came_from[current]
			else:
				path.insert(0,start)
			return path

		neighbors = get_neighbors(tilemap, current)
		for neighbor in neighbors:
			if neighbor not in came_from:
				frontier.put(neighbor)
				came_from[neighbor] = current
	return []

# dijkstra's algorithm
def dijkstra(tilemap, start, end):
	frontier = Queue.PriorityQueue()
	if position_passable(tilemap, start): frontier.put((0,start))
	came_from = {start:None}
	tentative_distance = {start:0}

	while frontier:
		current = frontier.get()[1]

		# check if current node is the destination
		if current == end: # if so, return path
			path = []
			while current != start:
				#print current
				path.insert(0,current)
				current = came_from[current]
			else:
				path.insert(0,start)
			return path

		for neighbor in get_neighbors(tilemap, current):
			if neighbor not in tentative_distance:
				new_dist = tentative_distance[current] + tilemap[neighbor[1]][neighbor[0]]
				frontier.put((new_dist, neighbor))
				tentative_distance[neighbor] = new_dist
				came_from[neighbor] = current
	return []

def greedy_best_first_search(tilemap, start, end):
	return []

def a_star(tilemap, start, end):
	return []