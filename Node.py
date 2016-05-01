class Node():
	def __init__(self):
		self.left_child = None
		self.right_child = None
		self.feature = None
		self.split_index = None
		self.impurity = 100000000000.0
		self.value = None