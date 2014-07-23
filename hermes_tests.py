import unittest, tilemap, pathfinders

# Unit testing module for hermes

class BFSTestCase1(unittest.TestCase):
	def runTest(self):
		tmap = tilemap.string_to_map('X0000X0\n0X0XXX0\n000110X\nXXXX000')
		start = (4,0)
		end = (6,3)
		
		path = pathfinders.breadth_first_search(tmap, start, end)
		assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3)])

if __name__ == '__main__':
	unittest.main()