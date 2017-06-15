'''
set-cover.py: Approximation set-cover algorithm.
'''

import matrix
import tp2io as tio

def cover(N, S, to_cover):
	''' Covers the points @to_cover considering the points set @S and the
		incidence matrix @N. Returns the remaining points to cover after this
		cover. '''
	points_index = [list(i) for i in zip(*N.data)][S]
	points = len(points_index)

	s_points = []

	for i in range(points):
		if (points_index[i] == 1):
			s_points.append(i)

	for p in s_points:
		to_cover.remove(p)

	return to_cover

def get_uncovered_points(C, N, points):
	''' Generates the list of uncovered points considering the current set
		cover @C, the incidence matrix @N and the number of @points. '''
	uncovered = [i for i in range(points)]

	for S in C:
		uncovered = cover()


def set_cover_algorithm(input, output):
	''' Set cover approximation algorithm. @input is the input file and
		@output is the ouput file. '''
	elem, sets, c, N = tio.read_initial_data(input)

	Cover = set()
	x = [0 for i in range(elem)]
	left_to_cover = [i for i in range(elem)]

	# TODO