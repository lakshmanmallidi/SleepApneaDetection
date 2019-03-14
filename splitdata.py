import pickle
filename = "ApneaData.csv"
f = open(filename,'rb')
data = f.read()
f.close()
rows = data.split(b"\n")
d = []
for row in rows:
    rowSplit = list(map(int,row.split(b" ")))
    d.append(rowSplit)
f = open('ApneaData.pkl','wb')
pickle.dump(d,f)
f.close()
