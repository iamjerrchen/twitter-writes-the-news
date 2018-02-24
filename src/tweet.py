import json

class Tweet:
    
    def __init__(self, raw_tweet):
        json_tweet = json.loads(raw_tweet)
        self.date = json_tweet["created_at"] 
        self.text = json_tweet["text"]
        self.screen_name = json_tweet["user"]["screen_name"]
        self.location = json_tweet["user"]["location"]
        self.verified = json_tweet["user"]["verified"]
        self.lang = json_tweet["user"]["lang"]
        self.truncated = json_tweet["truncated"]

    def disp(self):
        print u"name: {0}".format(self.screen_name)
        print u"date: {0}".format(self.date)
        print u"tweet: {0}".format(self.text)
        print u"location: {0}".format(self.location)

    def clean_text(self):
        cleaned = self.text
        # Remove RT
        cleaned = cleaned.replace("RT", "")

        words = cleaned.split(" ")
        cleaned_words = []
        for word in words:
            if not "@" in word and not "http" in word:
                cleaned_words.append(word)

        cleaned = " ".join(cleaned_words)

        return cleaned

