class Reader:
	def __init__(self, filePath):
		self.filePath = filePath
	
	# Abre o arquivo
	def open(self):
		self.file = open(self.filePath)

		return self
	
	# Pega o conteúdo
	def get_content(self):
		return self.file.read()