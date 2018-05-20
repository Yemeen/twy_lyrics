import read_file

from gensim.models import Word2Vec

from sklearn.decomposition import PCA
from matplotlib import pyplot

sentences = read_file.get_sentence_matrix()

# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
# print(model)
# summarize vocabulary
# words = list(model.wv.vocab)
# print(words)
# access vector for one word
# print(model['kyoto'])
# save model
# model.save('model.bin')
# load model
# new_model = Word2Vec.load('model.bin')
# print(new_model)

#### Visualize the model
# fit a 2d PCA model to the vectors
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()