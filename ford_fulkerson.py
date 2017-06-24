'''
ford_fulkerson.py: Ford-Fulkerson algorithm for maximum flow.
'''

import flow_network as fn
import tp2io as tio

def add_vertices_to_flow(num_v, flow):
	''' Adds all @num_v vertices to the @flow network object. '''
	for v in range(num_v):
		flow.add_vertex(v)

def add_edges_to_flow(c, N, flow):
	''' Adds all edges in incidence matrix @N to the @flow network object.
		The list @c indicates the capacity of each edge. '''
	for e in range(N.columns):
		column = N.get_column(e)
		vertices = (column.index(-1), column.index(1))
		new_edge = fn.Edge(vertices[0], vertices[1], c[e])
		flow.add_edge(new_edge)

def ford_fulkerson(input, output):
	''' Ford-Fulkerson algorithm for maximum flow. @input is the input file and
		@output is the output file. '''
	num_v, num_e, c, N = tio.read_initial_data(input)

	# Creates the flow network object.
	graph = fn.FlowNetwork()
	add_vertices_to_flow(num_v, graph)
	add_edges_to_flow(c, N, graph)

	for key, value in graph.edges.items():
	    print(key, value)

	print(graph.find_st_path(0, 3, []))