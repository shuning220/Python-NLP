from __future__ import division
import nltk
nltk.download()
from nltk.book import *


text1.concordance('monstrous')#display a word with its immediate context
text1.similar('monstrous')#find other words with similar context
text2.common_contexts(['monstrous','very'])#contexts shared by the two words

#text4.dispersion_plot(['citizens','democracy','freedom'])
x=len(text3)
print(x)

#sort all the vocabulary (unique)
sorted(set(text3))

#how many times a unique word is used
len(text3)/len(set(text3)

#word count
text3.count('the')

#define a function
def lexical_diversity(text):
    return len(text)/len(set(text))
def percent(count,total):
    return 100*count/total

#call function
lexical_diversity(text3)
percent(text4.count('the'),len(text4))

sentence1=['nltk','is','very','fun']
print(sorted(sentence1))
print(len(set(sentence1)))
print(lexical_diversity(sentence1))
sentence1.append('!!')

#indexing
text3[123];text3[0]
text3.index('wish')

#slicing
text3[1:144];text3[32:99]
text3[:53];text3[25:]
name_new='nltk'
name_new[0]
name_new*2
' '.join(['nltk','wonderful])
'nltk wonderful'.split()

fdist1=FreqDist(text3)
fdist1.plot(50,cumulative=True)
fdist1.hapaxes()#words that occur only once

V=set(text3)
long_words=[w for w in V if len(w)>10]
sorted(long_words)

#fine tuning
fdist5=FreqDist(text5)
sorted([y for y in set(text5) if len(y)>7 and fdist5[y]>5])

#collocations
text4.collocations()

#distribution of length of words
fdist2=FreqDist([len(w) for w in text1])
fdist2.keys()
fdist2.items()
fdist2.max()
fdist2[5]
fdist2.freq(2)#proportion of word with length of 2 in the whole text
fdist2.tabulate()
fdist2.N() #total number of samples

#operation
wordsel=[w for w in sent1 if len(w)<4]
wordsel=[w for w in sent1 if len(w)<=4]
wordsel=[w for w in sent1 if len(w)!=4]
wordsel=[w for w in sent1 if len(w)==4]
sorted([w for w in set(text1) if w.endswith('es')])
sorted([w for w in set(text1) if w.istitle()])
[w.upper() for w in text1]

#exercise
#1.
12/(4+1)

#2.
26**10
26**100

#3.
['Monty','Python]*3
3*sent1

#4.
len(text2)
len(set(text2))

#5.answer: romance
def lexical_div(text):
    return len(text)/len(set(text))
lexical_div(text2)
lexical_div(text3)

#6.
text2.dispersion_plot(['Elinor','Marianne','Edward','Willoughby']

#7.
text5.collocations()

#8.merge the duplicates; count the frequency

#9.
my_string='I want to have milk tea.'
my_string 
print(my_string)
my_string + my_string
(my_string +' ')*3

#10
my_sent=['My','sent']
my_sent1=' '.join(my_sent)
my_sent1.split()

#11.
p1=['apple','orange','cheery','strawberry']
p2=['coffee','milktea','coke']
if len(p1+p2)==len(p1)+len(p2):
    print ('yes')
else:
    print('no')

#12.
'Monty Python'[6:12]
['Monty','Python'][1]

#13.
sent1[2][2]

#14.
for i in range(len(sent3)):
    if sent3[i]=='the':
        print (i)

#15.
sorted([w for w in text5 if w.startswith('b')])

#16.
range(10)

#17.
text9.index('sunset')
text9[621:633]

#18
list=sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8
sorted(set(list))

#19.B is bigger
a=len(sorted(set([w.lower() for w in text1])))
b=len(sorted([w.lower() for w in set(text1)]))
a>b

#20
a=[w.isupper() for w in sent1]
b=[not w.islower() for w in sent1]

#21.
text2[-2:]

#22.
x=[y for y in text5 if len(y)==4]
fdist=FreqDist(x)
fdist.keys()

#23.
for i in range(len(text5)):
    if text5[i].isupper() is True:print (text5[i])

#24.
a=[w for w in set(text6) if w.endswith('ize') and 'z' in w and 'pt'in w]

#25.
list=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
[w for w in list if w.startswith('sh')]
[w for w in list if len(w)>4]

#26.
sum([len(w) for w in text1])/len(text1)

#27.
def vocab_size(text):
    return len(text)

#28.
def percent(count,total):
    return 100*count/total

percent(text4.count('the'),len(text4))

#29
set(sent3) < set(text1)