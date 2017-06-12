'''
tp2.py: Main program.
'''

import sys

NUM_ARGS = 4
SET_COVER = 's'
FORD_FULK = 'f'
ALG_INDEX = 1
INPUT_INDEX = 2
OUTPUT_INDEX = 3

def print_usage():
	''' Prints the program's correct usage. '''
	print('Usage: python3', sys.argv[0], '<algorithm> <input> <output>')
	exit()

def print_algorithm_choices():
	''' Prints the algorithms available for the user. '''
	print('Algorithms:', SET_COVER, 'for Set-Cover,', FORD_FULK, \
		'for Ford-Fulkerson.')
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
		print('[Error] Invalid algorithm choice.')
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

def set_cover():
	pass

def ford_fulkerson():
	pass

def main():
	''' Main program. '''
	# Checks arguments.
	algorithm = check_arguments()

	# Opens the input and output files.
	input_file = open_input_file(sys.argv[INPUT_INDEX])
	output_file = open_output_file(sys.argv[OUTPUT_INDEX])

	# Executes the selected algorithm.
	if (algorithm == SET_COVER):
		set_cover()
	if (algorithm == FORD_FULK):
		ford_fulkerson()

	# Closes files.
	input_file.close()
	output_file.close()

# Main execution.
main()