from nltk.corpus import stopwords
import PyPDF2

stop_words = set(stopwords.words('english'))
pdfFileObj = open('R:\MNIT\Django\example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
word_tokens = pageObj.extractText().split()
pdfFileObj.close()
word_tokens = list(dict.fromkeys(word_tokens))
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(filtered_sentence)



# stop_words = set(stopwords.words('english'))
# print(stop_words)
# word_tokens = example_sent.split()
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
# print(filtered_sentence)
