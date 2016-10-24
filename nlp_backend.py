from sys import argv
script, filename  = argv
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords


#opening the file and reading it!
txt = open(filename)
print "Here's your file %r:" %filename
ex_text =  txt.read()

#printing the tokenized sentences
print "\n The tokenized sentences are:"
tokenized_sent = sent_tokenize(ex_text)
print tokenized_sent

list_word = []          #consist of list of sentences tokenized into words
listiword = []          #contains list of all words in the ex_text

#Now, each word tokenized in the sentence:\n"
for s in tokenized_sent:
   words = word_tokenize(s)
   list_word.append(words)

#putting each word in ex_text into listiword
for l in list_word:
   for w in l:
      listiword.append(w)
print "\n"
print "This is listiword!"
print listiword
print "\n"

#The cleaned up paragraph
print "I am removing the stop_words!"
stop_words = set(stopwords.words("english"))
ex_text = [w for w in listiword if not w in stop_words]
print ex_text
print "\n"


#identifies the Names
def proper_nouns():
    tagged_sent = pos_tag(listiword)
    proper_noun1= [word for word, pos in tagged_sent if pos == 'NNP']
    dead_lines = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','January','February', ' March', 'April', 'May','June', 'July', ' August', ' September', 'October', 'November','December']
    names = [w for w in proper_noun1 if not w in dead_lines]
    return names

#identifies deadlines if any
def dead_lines():
    tagged_sent = pos_tag(listiword)
    proper_noun1= [word for word, pos in tagged_sent if pos == 'NNP']
    dead_lines = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','January','February', ' March', 'April', 'May','June', 'July', ' August', ' September', 'October', 'November','December']

    for w in proper_noun1:
      if w in dead_lines:
         print "The respective deadline is:",w



#identifying the sentences that consist of the names:
def sent_with_name():
    z = proper_nouns()
    for sent in tokenized_sent:
        word2 = word_tokenize(sent)
        t = any((True for x in word2 if x in z))
        if t == True:
            print sent

#calling out the functions clearly
print "Here are all the names"
z = proper_nouns()
print z
print "\n"

print "Here are the deadlines"
dead_lines()
print "\n"

print "These are the contexts for the respective names:"
sent_with_name()

#pos()
###def chunking():
##       for s in tokenized_sent:
##           words = word_tokenize(s)
##           tagged = nltk.pos_tag(words)
##           chunk_gram = r"""Chunk: {<NNP><PRP.?>*<NN>*<VB.?>}"""
###chunking together words
##           chunk_parser = nltk.RegexpParser(chunk_gram)
##           chunked = chunk_parser.parse(tagged)
##
##           print chunked
##           chunked.draw()
##
##
###def chunki_tag():
##   for s in tokenized_sent:
##      words = word_tokenize(s)
##      tagged = nltk.pos_tag(words)
##
##      namedEnt = nltk.ne_chunk(tagged)
##      namedEnt.draw()
###pos()
####chunking()
##
##chunki_tag()

