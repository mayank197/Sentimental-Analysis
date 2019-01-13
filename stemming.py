import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ["python","pythoner","pythoned","pythoning","pythonly"]

"""
for w in example_words:
    print(ps.stem(w))
"""

# Analyzing it more using sentence

new_text = "It is very important to be pythonly while you are pythoning with pyhton. All pythoners have pythoned poorly atleast once"

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

