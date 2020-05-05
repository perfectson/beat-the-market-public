import re
import nltk 
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem .porter import PorterStemmer
from sklearn.preprocessing.label import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import reuters

nltk.download("punkt")
nltk.download("stopwords", "data")
nltk.download("reuters")

nltk.data.path.append("data")



labelBinarizer = MultiLabelBinarizer()
#data_set= reuters.fileids()
data_target = labelBinarizer.fit_transform(data_set[u'topics'])
stopWords = stopwords.words("english")
charfilter = re.compile("[a-zA-Z]")

def simpleTokenizer(text):
	words = map(lambda word : word.lower(), word_tokenize(text))
	words = [word for word in words if word not in stopWords]
	tokens = (list(map(lambda token: PorterStemmer().stem(token),words)))
	ntokens = list(filter(lambda token: charfilter.match(token),tokens))
	return ntokens

vec = TfidfVectorizer(tokenizer=simpleTokenizer,max_features=1000,norm="12")

mytopics = [u'cocoa',u'trade',u'money-supply',u'coffee', u'gold'] 
data_set = data_set[data_set[u'topics'].map(set(mytopics).intersection).apply(lambda x : len(x)>0)]

docs = list(data_set[u'body'].values)
dtm= vec.fit_transform(docs)
