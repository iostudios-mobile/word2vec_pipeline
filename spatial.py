from __future__ import division

import h5py, os
import numpy as np
from scipy.spatial.distance import pdist
from scipy.misc import factorial

def random_hypersphere_point(dim):
    pts = np.random.normal(size=dim)
    return pts / np.linalg.norm(pts)

#exit()
from gensim.models.word2vec import Word2Vec
f_features = "collated/w2v.h5"
clf = Word2Vec.load(f_features)
X_word = clf.syn0[1000:2000]
dist_word = pdist(X_word,metric='cosine')
n,dim = X_word.shape
print X_word.shape

rand_pts = [random_hypersphere_point(dim) for _ in xrange(n)]
dist_rand = pdist(rand_pts,metric='cosine')

h5 = h5py.File("collated/document_scores.h5",'r')
X_doc = h5["unique"]["PLoS_bio"]
dist_doc = pdist(X_doc[1000:2000],metric='cosine')


import seaborn as sns
sns.distplot(dist_word, label="word tokens")
sns.distplot(dist_doc, label="w2vec document sums")
sns.distplot(dist_rand, label="random points")
sns.plt.legend()
sns.plt.show()

