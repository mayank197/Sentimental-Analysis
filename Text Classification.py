import nltk
import random                #To randomize the dataset

from nltk.corpus import movie_reviews

"""
documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)),category)
"""

# The above can be done in a one-liner

documents = [(list(movie_reviews.words(fileid)),category)
                    for category in movie_reviews.categories()
                    for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))        # 15 Most common words


print(all_words["stupid"])      # Find number of times the word "stupid" has appeared :  






















