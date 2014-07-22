
# standard BFS from startpoint to endpoint. 
def breadth_first_search(tilemap, start, end):
	try:
		if not isinstance(tilemap[start[1]][start[0]], int):
			return []
	except:
		return []

	height = len(tilemap)
	width = len(tilemap[0])

	frontier = [start]
	came_from = {start:None}

	while frontier:
		current = frontier.pop(0)

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

		(x,y) = current
		neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
		for neighbor in neighbors:
			if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < width and neighbor[1] < height:
				if isinstance(tilemap[neighbor[1]][neighbor[0]], int) and neighbor not in frontier and neighbor not in came_from:
					frontier.append(neighbor)
					came_from[neighbor] = current
	return []

# dijkstra's algorithm
def dijkstra(tilemap, start, end):
	try:
		if tilemap[start[1]][start[0]]:
			return []
	except:
		return []

	height = len(tilemap)
	width = len(tilemap[0])

	frontier = [start]
	came_from = {start:None}

	while frontier:
		current = frontier.pop(0)
		print current

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

		(x,y) = current
		neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]\
		#print neighbors
		for neighbor in neighbors:
			if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] >= 0 < width and neighbor[1] < height:
				print neighbor
				if not tilemap[neighbor[1]][neighbor[0]] and neighbor not in frontier and neighbor not in came_from:
					frontier.append(neighbor)
					came_from[neighbor] = current
		#print frontier
	return []

def greedy_best_first_search(tilemap, start, end):
	return []

def a_star(tilemap, start, end):
	return []