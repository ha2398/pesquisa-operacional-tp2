'''
matrix.py: Defines a matrix data structure.
'''

class Matrix:
	''' A simple bidimensional matrix. '''

	def __init__(self, r, c):
		self.rows = r
		self.columns = c
		self.data = []

	def from_file(self, file):
		''' Reads matrix' content from file. '''
		for row in range(self.rows):
			string = file.readline().strip().split()
			line = [int(x) for x in string]
			self.data.append(line[0:self.columns])

	def get_row(self, i):
		''' Gets the ith row of the matrix. '''
		return self.data[i]

	def get_column(self, i):
		''' Gets the ith column of the matrix. '''
		return [list(i) for i in zip(*self.data)][i]

	def __str__(self):
		string = '['

		for i in range(self.rows-1):
			string += str(self.data[i]) + '\n'

		string += str(self.data[self.rows-1]) + ']'

		return string