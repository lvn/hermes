import sys

# filereader
# A module to help with reading files into maps

# reads string into map (2d array of booleans)
def string_to_map(string):
	return [[True if char=='1' else False for char in line] for line in string.split('\n')]

# reads a plaintext file into a map 
def read_file_to_map(filename):
	with open(filename, 'r') as f:
		return string_to_map(f.read())
	return tile_map

if __name__ == '__main__':
	try:
		print read_file_to_map(sys.argv[1])
	except:
		pass