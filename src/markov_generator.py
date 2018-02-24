import numpy as np

class markov_text_generator:
	def __init__(self, text):
		self.cache = {} # dictionary to predict next word
		#self.state_size = state_size # 
		self.words = text.split()
		self.word_size = len(self.words)
		self._database() # populate dictionary with words

	def _pent(self):
		# generates triples from the given data string.
		# if string is: "What a lovely day"
		# generates: (What, a , lovely) and (a, lovely, day)
		if self.word_size < 5:
			return

		for i in range(self.word_size - 4):
			# like return but returns a generator to be used once
			yield (self.words[i], self.words[i+1], self.words[i+2], self.words[i+3], self.words[i+4])

	def _database(self):
		for w1, w2, w3, w4, w5 in self._pent():
			key = (w1, w2, w3, w4)
			if key in self.cache:
				# append word to existing key
				self.cache[key].append(w5)
			else:
				# add new key with word
				self.cache[key] = [w5]

	def generate_markov_text(self, size=100):
		seed = np.random.randint(0, self.word_size-5)
		# initial key is (w1, w2, w3, w4)
		w1, w2, w3, w4 = self.words[seed], self.words[seed+1], self.words[seed+2], self.words[seed+3]
		gen_words = [w1, w2, w3, w4]
		for i in xrange(size):
			# try to use the key
			try:
				w1, w2, w3, w4 = w2, w3, w4, np.random.choice(self.cache[(w1, w2, w3, w4)])
				gen_words.append(w4)
			except Exception as e:
				# start over with new start initial keys
				w1, w2, w3, w4 = self.words[seed], self.words[seed+1], self.words[seed+2], self.words[seed+3]
				continue
		return ' '.join(gen_words)

