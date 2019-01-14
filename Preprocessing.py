import nltk
import re
import string
from nltk.corpus import stopwords
from string import punctuation
from num2words import num2words
from nltk.stem import WordNetLemmatizer


def Preprocessing(data):
	data1 = decontracted(data)
	data2 = RemovePunc(data1)
	data3 = Tolower(data2)
	data4 = WordTokenization(data3)
	print(data4)
	return;




def WordTokenization(data): #split text on whitespaces & remove whitespaces
	nltk_tokens = nltk.wordpunct_tokenize(data)
	#print (nltk_tokens)
	return nltk_tokens;

def LineTokenization(data):
	nltk_tokens = nltk.sent_tokenize(data)
	#print (nltk_tokens)
	return nltk_tokens;

def Tolower(data):
	data = data.lower() 
	#print(data)
	return data;

def RemoveNumbers(data): 
	result = re.sub(r'\d+', '', data) 
	#print(result)
	return result;

def RemovePunc(data):
	result = data.translate(string.maketrans("",""), string.punctuation)
	#print(result)
	return result;

def RemoveStopWords(data): #Delet
	stop_words = set(stopwords.words('english'))
	tokens = nltk.word_tokenize(data)
	result = [i for i in tokens if not i in stop_words]
	#print (result)
	return result;

def Num2words(num):
	result = num2words(num)
	#print(result)
	return result;



wordnet_lemmatizer = WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
word = "" 
for w in nltk_tokens:
	word = word + " " + wordnet_lemmatizer.lemmatize(w)
#print "%s"%(word)

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


Preprocessing("Hey. I'm Reem, how you're?!!")

#test = "Hey I'm Yann, how're you and how's it going ? That's interesting: I'd love to hear more about it."
#print(decontracted(test))
# Hey I am Yann, how are you and how is it going ? That is interesting: I would love to hear more about it.

#WordTokenization("I\tam\tReem\n")
#LineTokenization("Hello. I am Reem. ")
#Tolower("REEM")
#RemoveNumbers("Iam 21 and I have 2 brothers")
#RemovePunc("I,^am!?/R'e*&%$m")
#RemoveStopWords("NLTK is a leading platform for building Python programs to work with human language data.")
#Num2words(33)

