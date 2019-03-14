import numpy as np
from sklearn import svm,naive_bayes,ensemble,linear_model
from sklearn.metrics import accuracy_score
import time
import pickle
filename = "ApneaData.pkl"
testPercent=20
features = []
classes = []
t = time.time()
f = open(filename,'rb')
data = pickle.load(f)
f.close()
np.random.shuffle(data)
for row in data:
    features.append(row[:-1])
    classes.append(row[-1])
inputLength = len(features)
testLength = int(inputLength*0.2)
train_features, train_classes=features[:-testLength], classes[:-testLength]
test_features,test_classes = features[-testLength:],classes[-testLength:]
print("preprocessing time:",(time.time()-t))
t=time.time()
clf=ensemble.RandomForestClassifier(n_estimators=30)
clf.fit(train_features,train_classes)
print("fitting time:",(time.time()-t))
t=time.time()
pred_classes=[]
for e in test_features:
    pred_classes.append(clf.predict([e])[0])
score = accuracy_score(pred_classes,test_classes)*100
print("predicting time:",(time.time()-t))
print("Accuracy:",score)
