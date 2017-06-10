"""
matrix.py: Defines a matrix data structure.
"""

class Matrix:
	""" A simple bidimensional matrix. """

	def __init__(self, r, c):
		self.rows = r
		self.columns = c
		self.data = []

	def fromFile(self, file):
		""" Reads matrix' content from file. """
		for row in range(self.rows):
			string = file.readline().strip().split()
			line = [int(x) for x in string]
			self.data.append(line[0:self.columns])

	def __str__(self):
		return str(self.data)