'''
tp2.py: Main program.
'''

import ford_fulkerson as ff
import tp2io as tio
import set_cover as sc
import sys

def main():
	''' Main program. '''
	# Checks arguments.
	algorithm = tio.check_arguments()

	# Opens the input and output files.
	input_file = tio.open_input_file(sys.argv[tio.INPUT_INDEX])
	output_file = tio.open_output_file(sys.argv[tio.OUTPUT_INDEX])

	# Executes the selected algorithm.
	if (algorithm == tio.SET_COVER):
		sc.set_cover_algorithm(input_file, output_file)
	if (algorithm == tio.FORD_FULK):
		ff.ford_fulkerson(input_file, output_file)

	# Closes files.
	input_file.close()
	output_file.close()

# Main execution.
main()