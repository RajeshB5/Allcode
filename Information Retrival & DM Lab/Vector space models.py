from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')
d1 = open("cc.txt", "r+").read()
d2 = open("fb.txt", "r+").read()

example_sent1 = d1

stop_words = set(stopwords.words('english'))

word_tokens1 = word_tokenize(example_sent1)

filtered_sentence = [w for w in word_tokens1 if not w in stop_words]

filtered_sentence = []

for w in word_tokens1:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)

term1 = d1.split()
term2 = d2.split()
totalTerms = list(set(term1) | set(term2))
dictionary1 = {}
dictionary2 = {}
for term in totalTerms:
    if term in d1:
        dictionary1[term] = 1
    else:
        dictionary1[term] = 0
    if term in d2:
        dictionary2[term] = 1
    else:
        dictionary2[term] = 0
vector1 = list(dictionary1.values())
vector2 = list(dictionary2.values())
dp = 0
ed = 0
md = 0
mod = 0
pnom1, pnom2 = 0, 0
for i in range(len(vector1)):
    dp += vector1[i] * vector2[i]
    pnom1 += vector1[i]**2
    pnom2 += vector2[i]**2
    ed += (vector1[i]-vector2[i])**2
    mod += (vector1[i] - vector2[i])**3
    md += abs(vector1[i]-vector2[i])
pnom1 = pnom1**0.5
pnom2 = pnom2**0.5
ed = ed**0.5
mod = mod**0.33
cosineDistance = dp/(pnom1*pnom2)
print(dictionary1, dictionary2)
print(vector1, vector2)
print("Cosign Distance ",cosineDistance)
print("Eucledian Distance ", ed)
print("Manhattan Distance ",md)
print(mod)