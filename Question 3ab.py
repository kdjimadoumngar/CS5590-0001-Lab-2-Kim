# 3. Write a programinwhich take an Input file. Use the simple approach below to summarize a text file:
# a. Read afile
# b. Apply lemmatization on the words
# c. Apply the bigram on the text
# d. Calculate the word frequency (bi-gram frequency) of the words (bi-grams)
# f. Choose top five bi-grams that have been repeated most
# g. Go through the original text that you had in the file
# h. Find all the sentences with those most repeated bi-grams
# i. Extract those sentences and concatenatej. Enjoy the summarization

## Importing the libraries

# #python
#
# import nltk, re
#
# #from nltk.corpus import wordnet as wn
#
# #from nltk.stem import PorterStemmer, WordNetLemmatizer
#
# nltk.download('wordnet')
#
# from nltk.stem.wordnet import WordNetLemmatizer
#
# import fileinput
#
# lemmatizer = WordNetLemmatizer()
#
# for line in fileinput.input('lem.txt',inplace=True, backup = '.bak'):
#     line =''.join(
#         [lemmatizer.lemmatize(w) for w in line.rstrip()]
#     )
#
# # # To overwrite line in file
#
#     print(line)


#############################################################################################

# from pywsd.utils import lemmatize_sentence
#
# lemmatize_sentence('These are foo bar sentences.')
#
# from _future_ import print_function
#
# from pywsd.util import lemmatize_sentence
#
# with open('myText.txt') as fin, open('lemout.txt', 'w') as fout
#     for line in fin:
#         print(' '.join(lemmatize_sentence(line.strip()), file = fout, end ='\n')

3######################################################################
import nltk

from nltk.stem import WordNetLemmatizer
#
# lemmatizer_output = WordNetLemmatizer()
# #
# lemmatizer_output.lemmatize('working')

#############################################################################
# ############# Bigram
#
import pandas as pd

#df = pd.read_txt('myText.txt')
#
# bigrams = tokens.apply(lambda x : list(nk.ngrams(x,2)))

##################################################################################################

#Get the frequency

from itertools import tee, islice

import re

from collections import Counter

words = re.findall("\w+", open('myText.txt').read())
def ngrams(lst, n):

    tlst = lst
    while True:
        a, b = tee(tlst)
        l = tuple(islice(a,n))

        if len(1) == n:

            yield 1

            next(b)

            tlst = b
        else:

            break

    print(Counter(zip(words, words[1:])))

