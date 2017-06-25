'''
tp2io.py: Defines que operations related to input and output.
'''

import matrix as m
import sys

NUM_ARGS = 4
SET_COVER = 's'
FORD_FULK = 'f'
ALG_INDEX = 1
INPUT_INDEX = 2
OUTPUT_INDEX = 3

def print_usage():
	''' Prints the program's correct usage. '''
	print('Usage:', sys.argv[0], '<algorithm> <input> <output>', \
		file=sys.stderr)
	exit()

def print_algorithm_choices():
	''' Prints the algorithms available for the user. '''
	print('Algorithms:', SET_COVER, 'for Set-Cover,', FORD_FULK, \
		'for Ford-Fulkerson.', file=sys.stderr)
	exit()

def check_arguments():
	''' Checks the correctness of the passed arguments.
		Returns the algorithm selected by the user. '''
	# Number of arguments.
	if (len(sys.argv) != NUM_ARGS):
		print('[Error] Incorrect number of parameters.', file=sys.stderr)
		print_usage()

	# Algorithm selection.
	algorithm = sys.argv[ALG_INDEX]
	if (algorithm != SET_COVER and algorithm != FORD_FULK):
		print('[Error] Invalid algorithm choice.', file=sys.stderr)
		print_algorithm_choices()

	return algorithm

def open_input_file(file_name):
	''' Opens and returns the input file with name @file_name. '''
	try:
		input_file = open(file_name, 'r')
		return input_file
	except FileNotFoundError:
		print('[Error] Input file was not found.', file=sys.stderr)
		exit()

def open_output_file(file_name):
	''' Opens and returns the output file with name @file_name. '''
	output_file = open(file_name, 'w')
	return output_file

def read_initial_data(input_file):
	''' Reads, from @input_file, and returns the initial data needed by the
		algorithms. '''
	l1 = int(input_file.readline())
	l2 = int(input_file.readline())
	c = [int(x) for x in input_file.readline().split()]
	N = m.Matrix(l1, l2)
	N.from_file(input_file)

	return l1, l2, c, N