import sys, random

# tilemap module

def print_usage():
	usage = '''usage: 
- python mapgen.py read [input_file]
- python mapgen.py generate [output_file] [width] [height] [seed]
'''
	print usage

# classifies a charater to a tile
def char_to_tile(char):
		return int(char) if char.isdigit() else None

# reads string into map (2d array of booleans)
def string_to_map(string):
	return [[char_to_tile(char) for char in line] for line in string.split('\n')]


# reads a plaintext file into a map 
def read_file_to_map(filename):
	with open(filename, 'r') as f:
		return string_to_map(f.read())
	return tile_map

# generates a random wxh map at filename,
def generate(w,h,seed='X111122345'):
	if not seed:
		raise Exception('invalid seed')

	tile_map = [[char_to_tile(random.choice(seed)) for i in xrange(w)] for j in xrange(h)]
	return tile_map
		

def generate_to_file(filename,w,h,seed='X111122345'):
	with open(filename, 'w') as f:
		f.write(generate(w,h,seed))
		f.write('\n')

# prints map to stdout, path is optional
def map_to_string(grid, path=[]):
	height = len(grid)
	width = len(grid[0])

	for coord in path:
		grid[coord[1]][coord[0]] = '-'

	def tile_to_char(tile):
		return (str(tile) if isinstance(tile,int) else ('-' if (tile == '-') else 'X'))

	# reconstructs a map back from a 2D array to a block string
	output = '\n'.join([''.join([tile_to_char(tile) for tile in row]) for row in grid])

	return output

def draw_map(grid, path=[]):
	print map_to_string(grid,path)

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