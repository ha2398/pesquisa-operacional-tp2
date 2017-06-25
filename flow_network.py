'''
flow_network.py: Defines a Flow Network data structure.
'''

class Edge:
	''' Directed edge. '''
	def __init__(self, n, v1, v2, c):
		''' Both @v1 and @v2 represent the vertices of the edge. @c indicates
			its capacity. @n is the edge's id. '''
		self.id = n
		self.source = v1
		self.target = v2
		self.capacity = c

	def __repr__(self):
		return 	'(' + str(self.id) + ', ' + str(self.source) + ', ' + \
				str(self.target) + ')'

class FlowNetwork:
	''' Flow network data structure. '''
	def __init__(self):
		''' flows is a dictionary that stores the edges with flow different
			than zero. edges is simply a dictionary indexed by vertex and that
			stores all the edges adjacent to that vertex. '''
		self.flows = {}
		self.edges = {}

	def add_vertex(self, v):
		''' Adds a vertex @v to the flow network. '''
		self.edges[v] = []

	def add_edge(self, e):
		''' Adds an edge @e to the flow network. This method also builds the
			residual graph of the flow network incrementally. '''
		v1 = e.source
		v2 = e.target
		c = e.capacity

		# Builds the backward edge
		backward = Edge(-1, v2, v1, 0)

		# Sets the edges as each other's reverse edge.
		e.reverse = backward
		backward.reverse = e

		self.edges[v1].append(e)
		self.edges[v2].append(backward)

		# All flows are initially zero.
		self.flows[e] = 0
		self.flows[backward] = 0

	def get_incident_edges(self, v):
		''' Returns the incident edges to vertex @v. '''
		return self.edges[v]

	def find_st_path(self, source, target, st_path):
		''' Finds a @st_path that goes from @source to @target and is able to 
			allow flow. @st_path is an accumulator list that stores the edges
			used on the path so far. '''
		# Checks if the st_path is already complete.
		if source == target:
			return st_path

		''' For each edge incident to @source, looks for those with residual
			flow greater than zero. This indicates that it is possible to push
			flow towards the path that starts with those edges. '''
		source_edges = self.get_incident_edges(source)
		for edge in source_edges:
			residual_flow = edge.capacity - self.flows[edge]

			if residual_flow > 0 and not (residual_flow, edge) in st_path:
				path = self.find_st_path(edge.target, target, \
					st_path + [(residual_flow, edge)])

				if path != None:
					return path