# Classe que representa uma posição dentro da fita, detalhe bacana que baseei meu código em uma lista duplamente ligada
class Position:
	def __init__(self, char):
		self.char = char
		self.prev = None
		self.next = None

	def __eq__(self, other):
		return self.char == other

	def __repr__(self):
		return self.char

# Classe responsável por armazenar o estado da fita, aonde o cabeçote (head) está, qual o simbolo que ele está apontando e os movimentos do mesmo
class Tape:
	def __init__(self, head):
		self.head = head

	def change_char(self, char):
		self.head.char = char

	def move_left(self):
		self.head = self.head.prev

	def move_right(self):
		self.head = self.head.next
	
