import nltk
import random                #To randomize the dataset

from nltk.corpus import movie_reviews
import pickle

documents = [(list(movie_reviews.words(fileid)),category)
                    for category in movie_reviews.categories()
                    for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]       # Top 3000 words

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)       #True if word is in dictionary

    return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# Comment out only if pickle file doesn't exist
# This code is used only if the pickle file has been saved

classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo Accuracy Percent : ", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

# To be used only if pickle file hasn't been made yet.
# Once made, use the corresponding above 3 lines

""" 
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier,save_classifier)
save_classifier.close()
"""


















