from alphabet import Alphabet
from state import State
from move import Move
from input import Input

# Classe da bagunça, aqui é realizado o tratamento do conteúdo do arquivo de entrada
class Parser:

	# Método responsável por pegar um raw text e retornar o alfabeto, estados, movimentações e entradas
	def parse(self, fileContent):
		lines = fileContent.split('\n')
		index = 0;

		alphabet = Alphabet(lines[index])
		index += 1

		numberOfStates = int(lines[index])
		index += 1
		states = self.__generateStates(numberOfStates)

		numberOfMoves = int(lines[index])
		index += 1
		moves = self.__generateMoves(lines[index:index + numberOfMoves])
		index += numberOfMoves


		numberOfInputs = int(lines[index])
		index += 1

		inputs = [Input(line) for line in lines[index:index + numberOfInputs]]

		return alphabet, states, moves, inputs

	# Método "privada" responsável por gerar os estados
	def __generateStates(self, numberOfStates):
		states = {}

		for i in range(1, numberOfStates + 1):
			states[i] = State(i)
		
		return states
	
	# Método "privada" responsável por gerar os movimentos
	def __generateMoves(self, moveLines):
		moves = {}

		for line in moveLines:
			currentState, readChar, writeChar, direction, towardsState = line.split(" ")

			currentState = int(currentState)
			towardsState = int(towardsState)
			move = Move(currentState, readChar, writeChar, direction, towardsState)

			if currentState in moves:
				moves[currentState].append(move)
			else:
				moves[currentState] = [move]
			
		return moves
