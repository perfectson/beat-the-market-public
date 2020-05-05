import re
import nltk
import nltk.data 
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
#from nltk.corpus import wordnet

nltk.download('stopwords')

#Tokenize text in sentence basic Ita + Eng
frase= "dog eating shoes. family fucking mad, again a short story."
fraseit= "Mangiarsi le scarpe fa bene. Hai scelto tu la ricetta? No zio Concetta."
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
italiantokenizer= nltk.data.load('tokenizers/punkt/italian.pickle')
entoken = tokenizer.tokenize(frase)
ittoken = italiantokenizer.tokenize(fraseit)
print("EN", entoken)
print("IT",ittoken)

#Tokenize  sentence into words basic Ita + Eng
sentTokenizer= TreebankWordTokenizer()
enwordtoken = sentTokenizer.tokenize(entoken[0])
itwordtoken = sentTokenizer.tokenize(ittoken[0])
print("EN",enwordtoken)
print("IT",itwordtoken)

#filter stopwords in tokenized sentence
english_stops= set(stopwords.words("english"))
ita_stops= set(stopwords.words("italian"))

filt_ita = [word for word in itwordtoken if word not in ita_stops]
filt_eng= [word for word in enwordtoken if word not in english_stops]
print("EN",filt_eng)
print("IT",filt_ita)

print("List of stopwords by language", stopwords.fileids())
print("italian stopwords:", ita_stops)

#It's possible to Create Custom Corpora

from nltk.corpus import wordnet
nltk.download('wordnet')

syn = wordnet.synsets("oil")[0]
print(syn.name," def: ",syn.definition())