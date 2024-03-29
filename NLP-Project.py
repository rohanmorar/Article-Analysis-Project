# Importing libraries
import nltk
import requests
import string
import matplotlib.pyplot as plt
from newspaper import Article
from newspaper import fulltext
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Importing Article
url = 'https://www.nbcnews.com/mach/science/israeli-scientists-create-world-s-first-3d-printed-heart-using-ncna996031'
article = Article(url)
article.download()


# Get full text
html = requests.get(url).text
text = fulltext(html)
#print(text)

#Tokenize word in text
tokenized_word = word_tokenize(text)
#print(tokenized_word)


# Import our stopwords to refrence with article
stop_words = set(stopwords.words("english"))
# print(stop_words)

# Function that allows us to come up with a list of filtered words.
words = word_tokenize(text)

filtered_sent = []
for w in words:
    if w not in stop_words:
        filtered_sent.append(w)
#print(filtered_sent)

#Remove punctuation from list.
filtered_sent = [''.join(c for c in s if c not in string.punctuation) for s in filtered_sent]

#Removes all spaces from list.
filtered_sent = [s for s in filtered_sent if s]


# Freq Dist Graph
fdist = FreqDist(filtered_sent)

fdist.plot(30,cumulative=False)
plt.show()

# Stemming words in article
ps = PorterStemmer()

for w in filtered_sent:
	print(ps.stem(w))

#POS Tagging
nltk.pos_tag(filtered_sent)

#Sentimental Analysis
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

# sentiment_analyzer_scores(text) to see pos neg and neu.

