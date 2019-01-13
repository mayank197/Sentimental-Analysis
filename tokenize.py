import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

example_sentence = "Hello there!! How are you ? The weather is great. Python is awesome. Take care"
print("Sentences are : \n%s" %sent_tokenize(example_sentence))
print("Words are : \n%s" %word_tokenize(example_sentence))


