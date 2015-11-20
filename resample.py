# -*-coding: utf-8 -*-
from NSE_Analytics_for_validation.util import great_circle_dist


class Resample(object):
	'''
	This is the class for resample 
	the one-direction route coordinate
	'''
	def __init__(self, path, radius):
		self.path = path
		self.radius = radius
		self.parse_path = [path[0]]

	def parse(self):
		'''discard the new coordinate in the previous circle'''
		for coordinate in self.path:
			if great_circle_dist(self.parse_path[-1],
					coordinate, 
					unit="meters") > self.radius:
				self.parse_path.append(coordinate)
		return self.parse_path

def main():
	'''Test'''

	path = [(103.9447, 1.31658), (103.94473, 1.31623), (103.9445, 1.31615), (103.94435, 1.31609), (103.94431, 1.31619), (103.94434, 1.31611), (103.94444, 1.31614), (103.94473, 1.31624), (103.94535, 1.31645), (103.94729, 1.31695), (103.94745, 1.317), (103.94789, 1.31718), (103.94849, 1.31743), (103.94883, 1.31755), (103.9508, 1.31819), (103.95139, 1.31834), (103.95214, 1.31851), (103.95277, 1.31868), (103.95279, 1.31868), (103.95309, 1.31876), (103.95403, 1.31922), (103.95498, 1.31968), (103.95519, 1.31979), (103.95521, 1.3198), (103.9555, 1.31994), (103.95572, 1.32004), (103.95582, 1.32013), (103.95588, 1.32036), (103.95587, 1.32047), (103.95581, 1.32056), (103.9555, 1.32095), (103.95528, 1.32124), (103.95473, 1.32194), (103.95458, 1.32213), (103.95421, 1.32259), (103.95388, 1.32306), (103.95319, 1.32397), (103.95291, 1.32435), (103.95202, 1.3255), (103.95124, 1.32652), (103.95116, 1.32662), (103.95081, 1.32714), (103.95042, 1.32762), (103.95022, 1.32786), (103.94991, 1.32808), (103.94975, 1.32816), (103.94924, 1.32818), (103.94901, 1.32819), (103.94737, 1.32757), (103.94638, 1.3272), (103.94636, 1.32719), (103.94627, 1.32716), (103.94414, 1.32634), (103.9431, 1.32598), (103.94211, 1.32565), (103.94155, 1.32546), (103.94081, 1.32531), (103.94069, 1.32529), (103.94053, 1.32526), (103.94032, 1.32641), (103.9398, 1.32909), (103.93973, 1.32944), (103.93961, 1.32942), (103.93971, 1.32944), (103.93979, 1.32901), (103.94012, 1.32908), (103.94105, 1.32926), (103.9411, 1.329)]
	radius = 20
	print len(path)
	resample = Resample(path, radius)
	path_after_parse = resample.parse()
	print len(path_after_parse)

if __name__ == "__main__":
	main()
