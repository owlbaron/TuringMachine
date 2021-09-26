from tape import Position

# Classe que representa um input
class Input:
	# Recebe uma lista de simbolos
	def __init__(self, i):
		self.input = i

	# Transforma a lista de simbolos em posições da fita
	def to_positions(self):
		inpuWithBlank = f"{self.input}-"

		positions = [Position(char) for char in inpuWithBlank]
		for index in range(len(positions)):
			if index - 1 >= 0:
				positions[index - 1].next = positions[index]
				positions[index].prev = positions[index - 1]
			
			if index + 1 < len(positions):
				positions[index].next = positions[index + 1]
				positions[index + 1].prev = positions[index]

		return positions

	def __repr__(self):
		return self.input
