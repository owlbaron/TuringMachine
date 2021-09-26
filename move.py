# Classe que representa uma movimentação na fita
class Move:

	# Recebe em seu construtor:
	# o estado atual;
	# qual o simbolo que está sendo lido;
	# qual o simbolo que vai ser escrito no lugar;
	# para qual direção o cabeçote vai;
	# estado de destino;
	def __init__(self, currentState, readChar, writeChar, direction, towardsState):
		self.currentState = currentState
		self.readChar = readChar
		self.writeChar = writeChar
		self.direction = direction
		self.towardsState = towardsState
	
	def __repr__(self):
		return f"{self.currentState} {self.readChar} {self.writeChar} {self.direction} {self.towardsState}"