#import data 
euro_16=pd.read_csv("euro_2016.csv",encoding="latin1")
euro_16.head(6)

#keras libraries 
import keras 
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD 
from sklearn.model_selection import train_test_split

#features and target data
euro_16x=euro_16[["home_win","home_score_diff","home_score_diff_date","away_score_diff",
"away_score_diff_date"]].values 

#subset 
X=euro_16x[:,1:5]
y=euro_16x[:,0]

X_train=X[14:51]
X_test=X[0:13]
y_train=y[14:51]
y_train=keras.utils.to_categorical(y_train)
y_test=y[0:13]
y_test=keras.utils.to_categorical(y_test)

#i. 
#keras multi-classfication model 
model=Sequential() 
model.add(Dense(5,activation="relu",input_dim=4))
model.add(Dropout(0.5)) #prevent overfitting 
model.add(Dense(5))
model.add(Dropout(0.2))
model.add(Dense(4,activation="softmax"))

sgd=SGD(lr=0.02,decay=1e-6,nesterov=True)
model.compile(loss="categorical_crossentropy",
optimizer=sgd,metrics=['accuracy'])

model.fit(X_train,y_train,epochs=12,batch_size=30)

score,acc=model.evaluate(X_test,y_test,batch_size-15)
acc 

#ii. keras binary classification 
euro_qual=pd.read_csv("wc14q1.csv",encoding="latin-1")
euro_qual.head(4)
euro_qual.info() 
euro_qual1=euro_qual[["team1_win","team_score_diff_t1","team_score_diff_date_t1","team_score_diff_t2","team_score_diff_date_t2"]].values 

X1=euro_qual1[:,1:5]
y1=euro_qual1[:,0]

X_train1=X1[14:51]
X_test1=X1[0:13]
y_train1=y1[14:51]
y_train1=keras.utils.to_categorical(y_train1)
y_test1=y1[0:13]
y_test1=keras.utils.to_categorical(y_test1)

#mlp binary classification
import numpy as np 
from keras.models import Sequential 
from keras.layers import Dense,Dropout 

model=Sequential()
model.add(Dense(5,input_dim=4,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(5))
model.add(Dense(2,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])
model.fit(X_train1,y_train1,epochs=12,batch_size=20) 

score,acc=model.evaluate(X_test1,y_test1,batch_size=20)
acc 