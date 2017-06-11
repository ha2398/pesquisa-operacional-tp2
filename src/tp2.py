'''
tp2.py: Main program.
'''

import sys

def print_usage():
	''' Prints the program's correct usage. '''
	print('Usage: python3', sys.argv[0], '<algorithm> <input> <output>')
	exit()

def print_algorithm_choices():
	''' Prints the algorithms available for the user. '''
	print('Algorithms: s for Set-Cover, f for Ford-Fulkerson.')
	exit()

def check_arguments():
	''' Checks the correctness of the passed arguments.
		Returns the algorithm selected by the user. '''
	# Number of arguments.
	if (len(sys.argv) != 4):
		print('[Error] Incorrect number of parameters', file=sys.stderr)
		print_usage()

	# Algorithm selection.
	algorithm = sys.argv[1]
	if (algorithm != 's' and algorithm != 'f'):
		print('[Error] Invalid algorithm choice.')
		print_algorithm_choices()

	return algorithm

def set_cover():
	pass

def ford_fulkerson():
	pass

def main():
	''' Main program. '''
	# Checks arguments.
	algorithm = check_arguments()

	if (algorithm == 's'):
		set_cover()
	if (algorithm == 'f'):
		ford_fulkerson()


# Main execution.
main()