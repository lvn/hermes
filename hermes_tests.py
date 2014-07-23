import unittest, tilemap, pathfinders

# Unit testing module for hermes

test_map_strings = [
'''X0000X0
0X0XXX0
000110X
XXXX000'''
]

test_maps = [tilemap.string_to_map(map_string) for map_string in test_map_strings]

class StringToMapTestCase1(unittest.TestCase):
	def runTest(self):
		assert(tilemap.string_to_map('X00\n012\nXYZ') == [[None, 0, 0], [0, 1, 2], [None, None, None]])

class BFSTestCase1(unittest.TestCase):
	def runTest(self):
		tmap = test_maps[0]
		start = (4,0)
		end = (6,3)

		path = pathfinders.breadth_first_search(tmap, start, end)
		assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3)])

class BFSTestCase2(unittest.TestCase):
	def runTest(self):
		tmap = test_maps[0]
		start = (5,0) # start tile is impassable
		end = (6,3)

		path = pathfinders.breadth_first_search(tmap, start, end)
		assert(path == []) # should return empty path since start tile is impassable

class DijkstraTestCase1(unittest.TestCase):
	def runTest(self):

		tmap = test_maps[0]
		start = (4,0)
		end = (6,3)

		path = pathfinders.dijkstra(tmap, start, end)
		assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3)])

if __name__ == '__main__':
	unittest.main()