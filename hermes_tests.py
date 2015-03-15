import unittest
import tilemap
import pathfinders

# Unit testing module for hermes

test_map_strings = ['''X1111X1
                    1X1XXX1
                    111111X
                    XXXX111''',
                    '''1111111
                    1111111
                    1122211
                    1121211
                    1122211
                    1111111
                    1111111''',
                    '''1111111
                    1XXXXX1
                    1X111X1
                    1X111X1
                    1X111X1
                    1X111X1
                    1111111''',
                    '''1111111
                    1111111
                    1122211
                    1112211
                    1122211
                    1111111
                    1111111''',
                    '''1111111
                    1113111
                    1233311
                    1111211
                    1111211
                    1111111
                    1111111'''
                    ]

test_maps = [tilemap.str_to_map(map_string) for map_string in test_map_strings]


class StringToMapTestCase1(unittest.TestCase):
    def runTest(self):
        assert(tilemap.str_to_map('X00\n012\nXYZ') ==
            [[None, 0, 0], [0, 1, 2], [None, None, None]])


class BFSTestCase1(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[0]
        start = (4, 0)
        end = (6, 3)

        path = pathfinders.breadth_first_search(tmap, start, end)
        assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3)])


class BFSTestCase2(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[0]
        start = (5, 0) # start tile is impassable
        end = (6, 3)

        self.assertRaisesRegexp(Exception, 'invalid starting position', pathfinders.breadth_first_search, tmap, start, end)
        #assert(path == []) # should return empty path since start tile is impassable


class BFSTestCase3(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[1]
        start = (3, 0)
        end = (3, 3)

        path = pathfinders.breadth_first_search(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3)])


class BFSTestCase4(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[2]
        start = (3, 0)
        end = (3, 2)

        path = pathfinders.breadth_first_search(tmap, start, end)
        assert(path == [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2)])


class BFSTestCase5(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[4]
        start = (3, 3)
        end = (3, 0)

        path = pathfinders.breadth_first_search(tmap, start, end)
        assert(path == [(3, 3), (3, 2), (3, 1), (3, 0)])


class DijkstraTestCase1(unittest.TestCase):
    def runTest(self):

        tmap = test_maps[0]
        start = (4, 0)
        end = (6, 3)

        path = pathfinders.dijkstra(tmap, start, end)
        assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3)])


class DijkstraTestCase2(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[1]
        start = (3, 0)
        end = (3, 3)

        path = pathfinders.dijkstra(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3)])


class DijkstraTestCase3(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[1]
        start = (3, 0)
        end = (3, 6)

        path = pathfinders.dijkstra(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])


class DijkstraTestCase4(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[2]
        start = (3, 0)
        end = (3, 2)

        path = pathfinders.dijkstra(tmap, start, end)
        assert(path == [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2)])


class DijkstraTestCase5(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[4]
        start = (3, 3)
        end = (3, 0)

        path = pathfinders.dijkstra(tmap, start, end)
        assert(path == [(3, 3), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0)])


class GreedyBFSTestCase1(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[0]
        start = (4, 0)
        end = (6, 3)

        path = pathfinders.greedy_best_first_search(tmap, start, end)
        assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3)])


class GreedyBFSTestCase2(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[1]
        start = (3, 0)
        end = (3, 3)

        path = pathfinders.greedy_best_first_search(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3)])


class AStarTestCase1(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[0]
        start = (4, 0)
        end = (6, 3)

        path = pathfinders.a_star(tmap, start, end)
        assert(path == [(4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (5, 3), (6, 3)])


class AStarTestCase2(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[1]
        start = (3, 0)
        end = (3, 3)

        path = pathfinders.a_star(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3)])


class AStarTestCase3(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[1]
        start = (3, 0)
        end = (3, 6)

        path = pathfinders.a_star(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])


class AStarTestCase4(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[2]
        start = (3, 0)
        end = (3, 2)

        path = pathfinders.a_star(tmap, start, end)
        assert(path == [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2)])


class AStarTestCase5(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[3]
        start = (3, 0)
        end = (3, 6)

        path = pathfinders.a_star(tmap, start, end)
        assert(path == [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])


class AStarTestCase6(unittest.TestCase):
    def runTest(self):
        tmap = test_maps[4]
        start = (3, 3)
        end = (3, 0)

        path = pathfinders.a_star(tmap, start, end)
        assert(path == [(3, 3), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0)])

'''
class RiverTestCase(unittest.TestCase):
    def runTest(self):
        tmap = tilemap.generate(50, 50)
        tilemap.draw_map(tmap, pathfinders.a_star(tmap, (0, 10), (49, 39)))
        assert(True)
'''

if __name__ == '__main__':
    unittest.main()
