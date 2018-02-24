# will need to run this the very first time to get stopwords file
# import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords
import markovify


class text_manipulator:
	def __init__(self):
		self.sw = set(stopwords.words('english')) # set of stopwords


	# removes common words, returns list of tokens
	def remove_stopwords(self, sentence):
		return filter(lambda word: not word in self.sw, sentence.split())

# testing stopword removal
# man = sentence_manipulator()
# man.remove_stopwords("a long string of text about him and her")

def generate_sentence(text):
	text_model = markovify.Text(text)
	for i in range(5):
		print(text_model.make_short_sentence(140))



