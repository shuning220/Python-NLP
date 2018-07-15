from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

url='http://www.gutenberg.org/files/2554/2554-0.txt'
raw=urlopen(url).read()
raw=raw.decode('utf-8')
type(raw)
len(raw)
raw.find('PART I')
raw.rfind('PART I')

tokens=nltk.word_tokenize(raw) #tokenization
type(tokens)

text=nltk.Text(tokens) #read it into text for further processing
type(text)
text[222:299]

#processing webpage
url='https://movie.douban.com/subject/27611429/'
html=urlopen(url).read()

from bs4 import BeautifulSoup
raw=BeautifulSoup(html)
raw=raw.get_text()
tokens = nltk.word_tokenize(raw)
text=nltk.Text(tokens)
text[2:10]

#local file
f=open('cd.txt')
raw=f.read()

#check the directory
import os
os.listdir('.')

#user input
s = input("Enter some text: ")
print ('You typed', len(nltk.word_tokenize(s)),'words.')

#string operation
sent="I ate a kiwifruit today."
sent.find('kiwifruit')
if "kiwifruit" in sent:
    print ("yes")
sent.index('kiwifruit')
sent.split()
sent.replace('kiwifruit','banana')

path=nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
import codecs
f=codecs.open(path,encoding='latin2')
f = codecs.open(path, 'w', encoding='utf-8')#write file

for line in f:
    line=line.strip()
    print (line.ecode('unicode_escape'))

import unicodedata
path='/users/shuninglu/nltk_data/corpora/udhr/Bosnian_Bosanski-Latin2'
lines=codecs.open(path,encoding='latin2').readlines()
line=lines[2]
print (line.encode('unicode_escape'))

#extracting words
word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]',word)
len(re.findall(r'[aeiou]',word))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj#loop for each word 
                      for vs in re.findall(r'[aeiou]{2,}',word))#find at least 2 of the vowels 
fd.items()

def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word
stem('friends')

re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')

from nltk.corpus import gutenberg, nps_chat
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r"<a> (<.*>) <man>") #find the word between a.. and man

chat = nltk.Text(nps_chat.words())
chat.findall(r"<.*> <.*> <bro>") #find three-word phrases ended with bro
chat.findall(r"<l.*>{3,}")#find three or more charater words starting with l

#nltk built-in stemmer
porter=nltk.PorterStemmer()
lanscaster=nltk.LancasterStemmer()
lemmn=nltk.WordNetLemmatizer()

#tokenizing
raw=raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone ... though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
... well without--Maybe it's always pepper that makes people hot-tempered,'..."""
re.split(r' ',raw)
re.split(r'[ \t\n]+', raw)#matches one or more space \t tab; \n new lines
re.split(r'\s+',raw)#any whitespace
re.split(r'\W+', raw) #focus on Word, punctuation not included
re.split(r'\w+', raw) #only punctuation
re.findall(r'\w+|\S\w*', raw) #match words, or puntuation with words 
re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)

#more efficient tokenizer
text='That U.S.A. poster-print costs $12.40....'
pattern=r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_]'''     
 #set flag to allow verbose regexps
         #abbr, e.g., U.S.A.
         #words with optional internal hyphens
         # currency and perceptage
        #ellipsis
    # separate tokens
    
nltk.regexp_tokenize(text, pattern)

#sentence segmentation
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')#load the tool
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)
import pprint
pprint.pprint(sents[171:181])

#print string and formatting
fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in fdist:
    print (word, '->', fdist[word], ';',)

'%s->%d;' % ('cat', 3) #insert-> into cat and 3
'%s->' % 'cat'  #%s insert after string, %d decimal
"%s wants a %s %s" % ("Lee", "sandwich", "for lunch")

template = 'Lee wants a %s right now'
menu = ['sandwich', 'spam fritter', 'pancake']
for snack in menu:
    print (template % snack)

'%6s' % 'dog'
'%-6s' % 'dog'
width = 6
'%-*s' % (width, 'dog')

count, total = 3205, 9375
"accuracy for %d words: %2.4f%%" % (total, 100 * count / total)#2.4 is floating point

#writing to files
output_file = open('output.txt', 'w')
words = set(nltk.corpus.genesis.words('english-kjv.txt'))
for word in sorted(words):
    output_file.write(word+'\n')
    output_file.write(str(len(words))+'\n')
output_file.close()

#1.
s='colorless'
s1=s[:4]
s2=s[4:]
'u'.join([s1,s2])

#2
re.split(r'-','fun-ny')[0]

#3
#Yes, if we [:-3] and the word only contains 2 characters

#4.
monty='There is a monty python.'
monty[1:11:2]
monty[11:1:-2]

#5.
monty[::-1]

#6.
monty='There is a 100% monty pi Python.'
nltk.re_show(r'[a-zA-Z]+',monty)
nltk.re_show(r'[A-Z][a-z]*',monty)#select a capitalized word
nltk.re_show(r'p[aeiou]{,2}t',monty)
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*',monty)
nltk.re_show(r'\w+|[^\w\s]+',monty)

#7.
x=r'^(the|a|an)$'
nltk.re_show(x,'the apple is big')
nltk.re_show(x,'the')


#8.

#9.


#10.
sent=['The','dog','gave','John','the','newspaper']
[(w, len(w)) for w in sent]

#11. 
monty='There is a 100% monty pi Python.'
monty.split('t')

#12. to be continuted