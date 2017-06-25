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
		new_edge = fn.Edge(e, vertices[0], vertices[1], c[e])
		flow.add_edge(new_edge)

def create_flow_network(num_v, c, N):
	''' Creates a flow network graph with the data read from file. @num_v
		indicates the number of vertices in the graph, @c represents the
		capacity of each edge in the graph, and @N is graph's incidence matrix.
		'''
	graph = fn.FlowNetwork()
	add_vertices_to_flow(num_v, graph)
	add_edges_to_flow(c, N, graph)

	return graph

def get_augmenting_flow(path):
	''' Returns the maximum possible flow value to augment in the graph,
		considering the augmenting @path. '''
	return min(residual for (residual, edge) in path)

def augment_flow(flow_network, path):
	''' Increases the flow in the @path considering the edge capacity
		constrainsts. '''
	augmenting_flow = get_augmenting_flow(path)
	for (residual_flow, edge) in path:
		flow_network.flows[edge] += augmenting_flow
		flow_network.flows[edge.reverse] -= augmenting_flow

def print_path(num_e, path, output):
	''' Prints a list of zeros and ones that represents the edges being used in
		the @path. The list is printed on @output. @num_e indicates the number
		of edges on the graph. '''
	edges = [0 for x in range(num_e)]
	for (flow, edge) in path:
		edges[edge.id] = 1

	print(edges, file=output)

def print_flows(flow_network, output):
	''' Prints a list of flows on the edges as is the current state of the
		@flow_network. The list is printed on @output. '''
	flows = [(edge.id, flow) for (edge, flow) in flow_network.flows.items()]
	flows = list(filter(lambda x: x[0] >= 0, flows))
	flows.sort(key=lambda tup: tup[0])
	flows = [x[1] for x in flows]

	print(flows, file=output)

def print_capacities(c, output):
	''' Print the list @c that represents the capacities of the edges on the 
		graph. The list is printed on @output. '''
	print(c, file=output)

def get_max_flow(graph):
	''' Returns the maximum flow running through the @graph. '''
	return sum(graph.flows[edge] for edge in graph.get_incident_edges(0))

def ford_fulkerson(input, output):
	''' Ford-Fulkerson algorithm for maximum flow. @input is the input file and
		@output is the output file. '''
	num_v, num_e, c, N = tio.read_initial_data(input)

	# Creates the flow network object.
	graph = create_flow_network(num_v, c, N)

	# Starts the algorithm.
	s = 0
	t = num_v - 1
	st_path = graph.find_st_path(s, t, [])

	''' Stops the algorithm when there is no longer an augmenting path from the
		source to sink. '''
	while st_path != None:
		print_path(num_e, st_path, output)
		augment_flow(graph, st_path)
		print_flows(graph, output)
		print_capacities(c, output)
		print('', file=output)
		st_path = graph.find_st_path(s, t, [])

	print('Maximum flow:', get_max_flow(graph), file=output)