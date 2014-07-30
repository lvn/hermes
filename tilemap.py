import sys, random

# tilemap module

def print_usage():
	usage = '''usage: 
- python mapgen.py read [input_file]
- python mapgen.py generate [output_file] [width] [height] [seed]
'''
	print usage

# reads string into map (2d array of booleans)
def string_to_map(string):
	return [[int(char) if char.isdigit() else None for char in line] for line in string.split('\n')]


# reads a plaintext file into a map 
def read_file_to_map(filename):
	with open(filename, 'r') as f:
		return string_to_map(f.read())
	return tile_map

# generates a random wxh map at filename,
def generate(filename,w,h,seed):
	if not seed: seed='XXXXX1123'
	with open(filename, 'w') as f:
		# f.write("%d %d" % (w,h))
		for y in xrange(h):
			for x in xrange(w):
				f.write(str(random.choice(seed)))
			f.write('\n')

# prints map to stdout, path is optional
def string_map(grid, path=[]):
	height = len(grid)
	width = len(grid[0])

	for coord in path:
		grid[coord[1]][coord[0]] = '-'

	# reconstructs a map back from a 2D array to a block string
	output = '\n'.join([''.join([(str(tile) if isinstance(tile,int) else ('-' if (tile == '-') else 'X')) for tile in row]) for row in grid])

	return output

def draw_map(grid, path=[]):
	print string_map(grid,path)

if __name__ == '__main__':
	try:
		if (sys.argv[1] == 'read'):
			print read_file_to_map(sys.argv[2])
		elif (sys.argv[1] == 'generate'):
			generate(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5])
		else:
			raise
	except:
		print_usage()