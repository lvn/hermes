import sys, filereader, pathfinders

# the command line interface: demonstrates how the pathfinding algorithms work.

algorithms = {
	'bfs': pathfinders.breadth_first_search,
	'breadth-first-search': pathfinders.breadth_first_search,
	'dijkstra': pathfinders.dijkstra,
	'greedy-bfs': pathfinders.greedy_best_first_search,
	'greedy-best-first-search': pathfinders.greedy_best_first_search,
	'a-star': pathfinders.a_star
}

def usage:
	print 'Usage: python hermes.py [algorithm] [input_file] [start_x] [start_y] [end_x] [end_y]'

if __name__ == '__main__':
	try:
		algorithm = algorithms[sys.argv[1]]
		tile_map = filereader.read_file_to_map(sys.argv[2])
		start = (sys.argv[3],sys.argv[4])
		end = (sys.argv[5],sys.argv[6])

		print algorithm(tile_map, start, end)
	except:
		usage()