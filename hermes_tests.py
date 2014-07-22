import unittest, filereader, pathfinders

# Unit testing module for hermes

class BFSTestCase1(unittest.TestCase):
	def runTest(self):
		tmap = filereader.string_to_map('1000010\n0101110\n0000001\n1111000')
		start = (4,0)
		end = (6,3)

		path = pathfinders.breadth_first_search(tmap, start, end)
		assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3)])

if __name__ == '__main__':
	unittest.main()