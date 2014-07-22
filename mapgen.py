import sys, random

# module for generating random maps.
# not really related to pathfinding, but I'm still including this here for now for testing purposes.

def usage():
	print 'usage: python mapgen.py [output] [width] [height] [seed]'

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
		generate(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
	except:
		usage()