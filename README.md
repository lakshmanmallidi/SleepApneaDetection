# Sleep Apnea Detection

In this project we will detect Sleep Apnea Detection using machine learning. We have two files ```main.py, splitdata.py, dataVisualization.py```. ```splitdata.py``` file is python 3.7 file used to split raw sleep apnea ecg data into python array and store it in ```ApneaData.pkl```. ```Main.py``` is main file where machine learning algorithms are implemented. ```dataVisualization.py``` graphically plots the data by using dimensionality reduction techniques.  
### Datasets

Sleep Apnea dataset consists of around 16000 people ECG data sampled at 6000 sample points each and 1 or 0 representing whether person have sleep Apnea or not. Data set structure looks like </br>
```
[
[0,1,2,.....,6000,cls],
[0,1,2,.....,6000,cls],
[0,1,2,.....,6000,cls],
...
...
...
..
[0,1,2,.....,6000,cls]
]
```
cls maybe 0 or 1. 1 respresents Apnea and 0 represents non Apnea.</br>

You can download dataset files from </br>
[Goolge drive link](https://drive.google.com/drive/folders/1sRE-iJFwQcOUNFJMUFM-17nH_xUFKoHa?usp=sharing)</br></br>
note: After downloading the datasets please copy them to the same folder where main.py and splitdata.py resides. ApneaData.pkl is generated from ApneaData.csv when you run splitdata.py .If you already downloaded both files no need to run splitdata.py file again. Directly run main.py.

### Dependencies

main.py needs scipy and numpy packages which you have to install through python package installer pip. open command prompt as admin and run </br>
```
pip install scipy 
pip install numpy 
```
note: Please install python 3.7 and don't forget to check add path while installing before installing packages.

### Algorithms

The algorithm we are using is ```ensemble.RandomForestClassifier``` from sklearn which is faster and more accurate. This algoritm is picked and tested with few other comparison. Feel free to change other algorithm classifier(clf) from sklearn. </br>

Using ```T-distributed Stochastic Neighbor Embedding``` algorithm to visualize data.



