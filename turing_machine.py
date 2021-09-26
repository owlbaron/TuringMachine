from tape import Tape

# Classe onde a mágica acontece
class TuringMachine:

	# Recebe a configuração da maquina
	def __init__(self, states, alphabet, moves, initialState, acceptableState):
		self.states = states
		self.alphabet = alphabet
		self.moves = moves
		self.currentState = initialState
		self.acceptableState = acceptableState
	
	# Método que inicia a execução da maquina
	def exec(self, i):
		# Transforma o input em posições da fita (lista duplamente ligada)
		positions = i.to_positions()

		# Inicia a fita com o cabeçote apontando para a primeira posição
		self.tape = Tape(positions[0])

		# Enquanto o cabeçote não estiver apontando pra none
		while self.tape.head != None:
			# Verifica se o simbolo do cabeçote pertence ao alfabeto
			if not self.alphabet.contains_char(self.tape.head):
				raise SyntaxError(f"Bad input {self.tape.head} is not included in alphabet")

			# Busca os possiveis movimentos para o estado atual
			possibleMoves = self.moves[self.currentState.name]

			# Variavel de controle para verificar se houve algum movimento nessa iteração
			moved = False
			
			# Procura dentre os movimentos possiveis aquele que atende o estado atual (simbolo apontado pelo cabeçote)
			for move in possibleMoves:
				# Caso um movimento seja encontrado
				if move.readChar == self.tape.head:
					# realiza-o
					self.move_head(move.direction, move.writeChar)
					# atualiza o estado
					self.currentState = self.states[move.towardsState]
					# atualiza a variavel de controle
					moved = True
					# sai do for da procura
					break
			
			# Caso a variavel de controle esteja False, a maquina não tem movimentos para aquele simbolo/estado, logo para-se a execução
			if not moved:
				break

		# Retorna se o estado encontrado é um estado de aceitação
		return self.currentState == self.acceptableState

	# Método responsável por realizar um movimento do cabeçote
	def move_head(self, direction, writeChar):
		# Escreve o novo simbolo na posição
		self.tape.change_char(writeChar)

		# Move o cabeçote para uma direção
		if direction == "D":
			self.tape.move_right()
		elif direction == "E":
			self.tape.move_left()
		else:
			raise SyntaxError(f"Bad input {direction} is an invalid move direction")
