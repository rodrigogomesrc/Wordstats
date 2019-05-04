class Wordstats(object):

	def __init__(self):

		"""
		This library provides statistis about the content of a file, such as words, lines, characters.

		To simplify and avoid duplicated words, the texts provided recieves treatment in order to eliminate 
		special characters accentuation and pontuation. Also, the code is not case sensitive.
		For this reason, this library is not indicated in cases that this differenciation is necessary.

		"""
		self.__special_characters = ['.',',',';',':','"','!','#','?','"',
		'@','_','-','[',']','{','}','%','©','+','-','=','*','&','/','º',
		'ª','”','“','(',')',]

 
	def __test_file(self, file_path):

		#test if the files exist. if it doesn't it will create one with the same path

		try:

			file = open(file_path, 'r')
			text = file.readlines()
			file.close()

		except:

			file = open(file_path, 'r')
			file.close()


	def __change_characters(self, text):

		"""
		Receives a string, remove special characters and separete words into tuples
		
		"""

		#to make the text not case sensitive

		text = text.lower() 

		new_text = ""

		#remove the unwanted characters

		for character in text:

			if character not in self.__special_characters:

				new_text += character

		#turn the text into a tuple of words

		new_text = new_text.split()

		return new_text
	

	def __array_stringfy(self, text):

		"""
		Receives a array of strings and make them into one string
		
		"""

		temp_text = ""

		for n in range(len(text)):

			temp_text += text[n];

		new_text = temp_text

		return new_text
	       
	

	def print_file(self, file_path):

		file = open(file_path, 'r')
		text = file.readlines()


		print(text)
		file.close()


	def word_frequence(self, word, file_path):

		"""
		Returns a int representing how many times a word appear on the file.

		"""

		pass


	def words_frequency(self,words_range):

		"""
		Returns the frequency of every word ordened by the frequency. the argument "words_range" limits how mahy words is shown.

		"""

		pass

	def words_count(self, file_path):

		"""
		
		Returns how many words are written on the document.

		"""
		self.__test_file(file_path)
		file = open(file_path, 'r')
		text = file.readlines()

		#turn the array into a string
		text = self.__array_stringfy(text)

		#turn the array int a tuple of words
		text = self.__change_characters(text)

		words = 0
		for word in text:

			words += 1;


		file.close()

		return words

	def lines_count(self, file_path):


		"""
		Returns how many lines are on the document.
		"""

		self.__test_file(file_path)
		file = open(file_path, 'r')
		text = file.readlines()
		lines = 0

		for line in text:

			lines += 1


		file.close()

		return lines

	def characters_count(self,file_path):

		self.__test_file(file_path)
		file = open(file_path, 'r')
		text = file.readlines()
		text = self.__array_stringfy(text)

		characters = 0

		for c in text:
			characters += 1

		
		file.close()

		return characters

	def characters_count_ns(self,file_path):


		"""
		Returns how many characters are on the document (not counting the space between words)
		"""

		
		self.__test_file(file_path)
		file = open(file_path, 'r')
		text = file.readlines()
		text = self.__array_stringfy(text)

		characters = 0

		for c in text:

			if c != " ":
				
				characters += 1

		
		file.close()

		return characters
