import nltk
nltk.corpus.gutenberg.fileids()

emma=nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))#need for corpus concordance
emma.concordance('suprise')

#alternative import
from nltk.corpus import gutenberg
gutenberg.fileids()
emma=gutenberg.words('austen-emma.txt')

#loop over the text to get information
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print (int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)

#webtext in nltk.corpus
from nltk.corpus import webtext
for filleid in webtext.fileids():
    print (fileid, webtext.raw(fileid)[:2])

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

#brown corpus
from nltk.corpus import brown
brown.categories()
brown.words(categories='editorial')
brown.words(fileids=['cp12'])
brown.sents(categories=['news','editorials'])

edi_text = brown.words(categories='fiction')
fdist=nltk.FreqDist([w.lower() for w in edi_text])
modals=['what','who','where','when','why']
for m in modals:
    print (m + ':', fdist[m])

#Reuters corpus
from nltk.corpus import reuters
reuters.fileids()
reuters.categories()
reuters.words('training/9947')[:14]
reuters.words(categories=['sorghum','rye'])

#inaugural address
from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))
cfd.plot()

#udhr corpus
from nltk.corpus import udhr
languages=['Chickasaw', 'English', 'German_Deutsch']
cfd=nltk.ConditionalFreqDist(
    (lang,len(word))
    for lang in languages
    for word in udhr.words(lang +'-Latin1'))
cfd.plot(cumulative=True)

#load your own corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root='/users/shuninglu/desktop'
wordlists=PlaintextCorpusReader(corpus_root,'.*')
wordlists.fileids()

#conditional freq distribution
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genre_word=[(genre,word)
            for genre in ['news','romance']
            for word in brown.words(categories=genre)]
len(genre_word)
genre_word[:4]

cfd=nltk.ConditionalFreqDist(genre_word)
cfd
cfd.conditions()
cfd['news']
cfd['romance']['could']

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in ['news','romance']
    for word in brown.words(categories=genre)])

cfd.tabulate(conditions=['news','romance'],samples=days,cumulative=True)

#generating random text 
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven','and', 'the', 'earth', '.']
nltk.bigrams(sent)

#function
#from filename import functionname

#stopwords
from nltk.corpus import stopwords
stopwords.words('english')

def content_fraction(text):
    stopwords=nltk.corpus.stopwords.words('english')
    content=[w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

content_fraction(udhr.words())

#sense and synonyms
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names() # a collection of synonymous words
wn.synset('car.n.01').definition()
for synset in wn.synsets('car'):
    print (synset.lemma_names())

#exercise
#1.
phrase=['I','came','back','late','today']
phrase +['.']
phrase*2
phrase[3]
phrase[2:]
sorted(phrase)

#2. 
persuasion=nltk.corpus.gutenberg.words('austen-persuasion.txt')
len(persuasion)
len(set(persuasion))

#3.
from nltk.corpus import brown
brown.fileids()
brown.categories()
brown.words(categories='adventure')

#4.
from nltk.corpus import state_union

text = state_union.words()
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men','women']
    if w.lower().startswith(target))
cfd.plot()

#5.
wn.synset('fish.n.01').part_meronyms()
wn.synset('fish.n.01').member_meronyms()
wn.synset('leaf.n.01').substance_meronyms()
wn.synset('fish.n.01').member_holonyms()
wn.synset('leaf.n.01').substance_holonyms()

#6.cannot translate among 3 languages at a time, loop to solve
from nltk.corpus import swadesh

cmp3= swadesh.entries(['fr', 'en','it'])
translate=dict(cmp3)
translate['chien']

languages = ['en', 'de','it']
for i in [39,132,193]:
    print (swadesh.entries(languages)[i])

#7.
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance('however')

#8.
names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()

#9.
emma=nltk.corpus.gutenberg.words('austen-emma.txt')
persuasion=nltk.corpus.gutenberg.words('austen-persuasion.txt')

def report(a):
    num_vocab = len(set([w.lower() for w in a]))
    voc_rich = len(a)/len(set(a))
    stopwords=nltk.corpus.stopwords.words('english')
    content=[w for w in a if w.lower() not in stopwords and w.isalpha()]
    fdist1=FreqDist(content)
    return num_vocab, voc_rich,voc_rich, fdist1.most_common(5)

report(emma)
report(persuasion)

#10.
from __future__ import division

def third_of_tokens(text):
    words_in_text = [w for w in text if any(c.isalpha() for c in w)]

    fd = nltk.FreqDist(words_in_text)
    most = fd.most_common(1000)
    count = 0
    third_words = []

    for word, num in most:
        if ((count < (len(words_in_text) / 3)) & any(c.isalpha() for c in word)):
            count = count + num
            third_words.append(word)
    print third_words        
    print len(third_words)
    
third_of_tokens(movie)

#11.
pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they']
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor', 'editorial', 'belles_lettres', 'government']
cfd.tabulate(conditions=genres, samples=pronouns)

#12.
count_distinct = 0
dublettes = []
prev = ''
for entry in nltk.corpus.cmudict.entries():
    if ((entry[0] == prev) and (entry[0] not in dublettes)):
        dublettes.append(entry[0])
    else: 
        count_distinct = count_distinct + 1
        prev = entry[0]
print count_distinct
print (len(dublettes) / count_distinct) * 100

#13.
all_syns = list(wn.all_synsets('n'))
no_hyponyms = [s for s in all_syns if len(s.hyponyms()) == 0]
print (len(no_hyponyms) / len(all_syns)) * 100

#14.
def supergloss(s):
    gloss = 'definition: ' + s.definition() + '\n\n'
    gloss = gloss + 'Hypernyms:\n'
    for hypernym in s.hypernyms():
        gloss = gloss + hypernym.name() + ': ' + hypernym.definition() + '\n'
    gloss = gloss + '\nHyponyms:\n'
    for hyponym in s.hyponyms():
        gloss = gloss + hyponym.name() + ': ' + hyponym.definition() + '\n'
    return gloss

print  superglosssuperglo (wn.synset('bicycle.n.01'))

#15.
edi_text = brown.words()
fdist3=FreqDist(edi_text)
sorted([y for y in set(edi_text) if fdist3[y]>2])

#16.
def lexcical_diversity(text):
    return len(text)/len(set(text))

for genre in nltk.corpus.brown.categories():
    print (genre + ': ' + str(lexical_diversity(brown.words(categories=genre))))

#17.
persuasion=nltk.corpus.gutenberg.words('austen-persuasion.txt')

from nltk.corpus import stopwords
stopwords.words('english')

def content_clear(text):
    stopwords=nltk.corpus.stopwords.words('english')
    content=[w for w in text if w.lower() not in stopwords and w.isalpha()]
    fdist = FreqDist(content) #if FreqDist is not defined, need to import nltk.book
    return fdist.most_common(5)

content_clear(persuasion)

#18.
def comm_bigram (text):
    stopwords=nltk.corpus.stopwords.words('english')
    content=[w for w in text if w.lower() not in stopwords and w.isalpha()]
    bi_gram= nltk.bigrams(content)
    fdist = FreqDist(bi_gram)
    return fdist.most_common(50)

comm_bigram(emma)

#19.
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres= ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals= ['I','you','he','she','we','they']
cfd.tabulate(conditions=genres,samples=modals)

#20.
def word_freq(text,word):
    return text.index(word)

word_freq(brown.words(categories='news'),'happy')

#21.
prondict = nltk.corpus.cmudict.dict()
    
def sum_syllables(text):
    count_syllables = 0
    for word in text:
        if any(c.isalpha() for c in word):
            try:
                pron = prondict[word.lower()][0]
            except KeyError:
                print '"' + word.lower() + '" does not exist in CMU!'
                continue
            else:    
                for syllable in pron:
                    if any(c.isnumeric() for c in syllable):
                        count_syllables = count_syllables + 1
    return count_syllables

sum_syllables(['She', 'sells', 'seashells', 'by', 'the', 'seashore'])

#22.
def hedge(text):
    text_hedged = []
    count = 0
    for word in text:
        text_hedged.append(word)
        count = count + 1
        if count == 3:
            text_hedged.append('like')
            count = 0
    return text_hedged

hedge(emma)

#23.to be continuted...

