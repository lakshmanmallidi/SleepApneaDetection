import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

filename = "ApneaData.pkl"
features = []
classes = []
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
f = open(filename,'rb')
data = pickle.load(f)
f.close()
for row in data:
    features.append(row[:-1])
    classes.append(row[-1])
reduced_features = TSNE(n_components=3).fit_transform(features)
classification = {0:[],1:[]}
colors = ('g','r')
for i in range(len(classes)):
    if classes[i]==0:
        classification[0].append(reduced_features[i])
    else:
        classification[1].append(reduced_features[i])
for i in classification.keys():
    x = []
    y = []
    z = []
    for e in classification[i]:
        x.append(e[0])
        y.append(e[1])
        z.append(e[2])
    ax1.scatter(x,y,z,c=colors[i])
plt.show()