# Classe de dado que representa um estado, por exemplo: Q1
class State:
	def __init__(self, name):
		self.name = name
	
	def __eq__(self, other):
		return self.name == other

	def __repr__(self):
		return self.name
	
	def __str__(self):
		return f"q{self.name}"