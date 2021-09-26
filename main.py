from reader import Reader
from parser import Parser
from turing_machine import TuringMachine

print("> Welcome to the turing machine")

# Pega o file path do arquivo que possui a configuração da maquina
filePath = input("> Please provide the file path of your input file (e.g. ./input.txt)\n> ")

# Em caso do file path estar vázio, utiliza um valor default
if filePath == "":
	filePath = "./input.txt"

# Com o file path em mãos chama a classe reader, que é responsável por abrir o arquivo e pegar o conteúdo
fileContent = Reader(filePath).open().get_content()

# Com o conteúdo do arquivo em mãos utilizamos o parser para montar toda nossa configuração da maquina, são eles o alfabeto, estados, movimentos e entradas
alphabet, states, moves, inputs = Parser().parse(fileContent)

# Percorremos as entradas disponibilizadas no arquivo
for index, i in enumerate(inputs):
	tm = TuringMachine(states, alphabet, moves, states[1], states[len(states.keys())])

	# Executamos a maquina
	okay = tm.exec(i)

	# Imprimimos o resultado
	if okay:
		print(f"{index + 1}: {i} OK")
	else:
		print(f"{index + 1}: {i} not OK")

