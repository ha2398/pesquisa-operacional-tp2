'''
flow_network.py: Defines a Flow Network data structure.
'''

class Edge:
	''' Directed edge. '''
	def __init__(self, v1, v2, c):
		''' Both @v1 and @v2 represent the vertices of the edge. @c indicates
			its capacity. '''
		self.source = v1
		self.target = v2
		self.capacity = c

	def __repr__(self):
		return '(' + str(self.source) + '->' + str(self.target) + ', ' + str(self.capacity) + ')\n'

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
		backward = Edge(v2, v1, 0)

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