import numpy as np

class markov_text_generator:
	def __init__(self, text, state_size):
		self.cache = {} # dictionary to predict next word
		self.state_size = state_size # 
		self.words = text.split()
		self.word_size = len(self.words)
		self.database() # populate dictionary with words

	def triples(self):
		# generates triples from the given data string.
		# if string is: "What a lovely day"
		# generates: (What, a , lovely) and (a, lovely, day)
		if self.word_size < 3:
			return

		for i in range(self.word_size - 2):
			# like return but returns a generator to be used once
			yield (self.words[i], self.words[i+1], self.words[i+2])

	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				# append word to existing key
				self.cache[key].append(w3)
			else:
				# add new key with word
				self.cache[key] = [w3]

	def generate_markov_text(self, size=100):
		seed = np.random.randint(0, self.word_size-3)
		# initial key is (w1, w2)
		w1, w2 = self.words[seed], self.words[seed+1]
		gen_words = [w1, w2]
		for i in xrange(size):
			w1, w2 = w2, np.random.choice(self.cache[(w1, w2)])
			gen_words.append(w2)
		return ' '.join(gen_words)

