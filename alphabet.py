# Representa o alfabeto da maquina
class Alphabet:
	# Recebe uma lista em seu construtor, contendo os simbolos permitidos
	def __init__(self, alphabet):
		self.data = alphabet
	
	# Método responsável por verificar se um simbolo faz parte do alfabeto, aqui incluimos também o simbolo terminal
	def contains_char(self, char):
		char = str(char)

		return self.data.find(char) >= 0 or char == '-'
