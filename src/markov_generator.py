import numpy as np

class markov_text_generator:
	def __init__(self, text, state_size):
		self.cache = {} # dictionary to predict next word
		self.state_size = state_size # 
		self.words = text.split()
		self.word_size = len(self.words)
		self._database() # populate dictionary with words

	def _n_state(self):
		# generates n size tuples from the given data string.
		# increasing state_size will match sentence closer to the data set
		# if state_size is 3 and string is: "What a lovely day"
		# generates: (What, a , lovely) and (a, lovely, day)
		if self.word_size < self.state_size + 1:
			return

		for i in range(self.word_size - self.state_size):
			# like return but returns a generator to be used once
			yield tuple([self.words[i+idx] for idx in range(self.state_size + 1)])

	# populate cache with keys and predicted next word
	def _database(self):
		# returns a tuple
		for key_data in self._n_state():
			key = tuple([key_data[k_idx] for k_idx in range(self.state_size)])

			if key in self.cache:
				# append word to existing key
				self.cache[key].append(key_data[self.state_size])
			else:
				# add new key with word
				self.cache[key] = [key_data[self.state_size]]

	def generate_markov_text(self, size=100):
		# pick random words
		seed = np.random.randint(0, self.word_size-self.state_size+1)
		# initial key
		word_key = [self.words[seed + idx] for idx in range(self.state_size)]
		# w1, w2, w3, w4 = self.words[seed], self.words[seed+1], self.words[seed+2], self.words[seed+3]
		gen_words = word_key
		for i in xrange(size):
			# try to use the key
			try:
				# get next word
				next_word = np.random.choice(self.cache[tuple(word_key)])

				# construct key for next iteration
				word_key = [word_key[idx+1] for idx in range(self.state_size-1)]
				word_key.append(next_word)

				# append new word
				gen_words.append(next_word)
			except Exception as e:
				# start over with new start initial keys
				word_key = [self.words[seed + idx] for idx in range(self.state_size)]
				continue
		return ' '.join(gen_words)

