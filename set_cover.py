'''
set_cover.py: Approximation set-cover algorithm.
'''

import matrix
import tp2io as tio

def cover_points(N, S, to_cover):
	''' Covers the points @to_cover considering the points set @S and the
		incidence matrix @N. Returns the remaining points to cover after this
		cover. '''
	points_index = N.get_column(S)
	points = len(points_index)

	s_points = []

	for i in range(points):
		if (points_index[i] == 1):
			s_points.append(i)

	for p in s_points:
		if p in to_cover:
			to_cover.remove(p)

	return to_cover

def get_uncovered_points(C, N, points):
	''' Generates the list of uncovered points considering the current set
		cover @C, the incidence matrix @N and the number of @points. '''
	uncovered = [i for i in range(points)]

	for s in C:
		uncovered = cover()

def get_point_sets(N, point):
	''' Returns a list that represents the sets that cover the @point. Each
		element on this list will be a tuple. The first element of this tuple
		is the number of the set and the second element is a list of indices
		of the points that this set covers. @N is the incidence matrix. '''
	point_sets = []
	sets_index = N.get_row(point)

	for i in range(len(sets_index)):
		if sets_index[i] == 1:
			point_sets.append((i, N.get_column(i)))

	return point_sets

def get_maximum_x(X, c, point, point_sets):
	''' Obtains the maximum value that can be assigned to @point's entry on
		the vector @X and the set associated with it. This is done considering
		the sets' cost vector @c, the @point being considered and the list
		@point_sets that represents the sets that cover @point. '''
	possible_values = []

	for s in point_sets:
		value = c[s[0]]
		indices = s[1]

		for i in range(len(indices)):
			if indices[i] == 1:
				value -= X[i]

		possible_values.append((s[0],value))

	possible_values.sort(key=lambda tup: tup[1])

	return possible_values[0][1], possible_values[0][0]

def select_next_set(N, X, c, point):
	''' Selects and returns the next set to add to the current cover. '''
	point_sets = get_point_sets(N, point)
	max_x, next_set = get_maximum_x(X, c, point, point_sets)

	# Updates the point's entry on X.
	X[point] = max_x

	return next_set

def get_cover_cost(cover, c):
	''' Returns the cost of the set @cover considering the cost of each set as
		represented in @c. '''
	cost = 0

	for s in cover:
		cost += c[s]

	return cost

def set_cover_algorithm(input, output):
	''' Set cover approximation algorithm. @input is the input file and
		@output is the ouput file. '''
	elem, sets, c, N = tio.read_initial_data(input)

	cover = set()
	X = [0 for i in range(elem)]
	Y = [0 for i in range(sets)]
	left_to_cover = [i for i in range(elem)]

	print('y:', Y)
	print('x:', X)

	while len(left_to_cover) != 0:
		print('\n')
		next_point = left_to_cover[0] # TODO: Randomize point choice.
		next_set = select_next_set(N, X, c, next_point)
		cover.add(next_set)
		Y[next_set] = 1
		left_to_cover = cover_points(N, next_set, left_to_cover)

		print('y:', Y)
		print('x:', X)

	print('Cost:', get_cover_cost(cover, c))