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
	if not seed: seed='0000011'
	with open(filename, 'w') as f:
		# f.write("%d %d" % (w,h))
		for y in xrange(h):
			for x in xrange(w):
				f.write(str(random.choice(seed)))
			f.write('\n')

if __name__ == '__main__':
	try:
		if (sys.argv[1] == 'read'):
			print read_file_to_map(sys.argv[2])
		elif (sys.argv[1] == 'generate'):
			generate(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5])

	except:
		print_usage()