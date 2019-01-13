from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))

print(lemmatizer.lemmatize("better"))                   # Prints 'better'
print(lemmatizer.lemmatize("better",pos="a"))       # Prints 'good' because POS is adjective

print(lemmatizer.lemmatize("best",pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",pos="v"))
