
#برسی دقیق داده ها
import pandas as pd
train=pd.read_csv("train.csv")

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
train["date"]=le.fit_transform(train["date"])

cols=[col for col in train.columns if col not in ['weather']]
data=train[cols]
target=train['weather']

from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(data, target, train_size=0.7, test_size=0.3)


from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
gnb=GaussianNB()
gnb.fit(data_train,target_train)
pred=gnb.predict(data_test)
print("accuracy_score:",accuracy_score(target_test,pred,normalize=True))



#شناسایی نقاط پرت با svm
import pandas as pd
train=pd.read_csv("train.csv")

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
train["date"]=le.fit_transform(train["date"])

cols=[col for col in train.columns if col not in ['weather']]
data=train[cols]
target=train['weather']

from sklearn.model_selection import train_test_split
data_train,data_test,target_train,target_test=train_test_split(data,target,train_size=0.7,test_size=0.3)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(data_train)
data_train_std=sc.transform(data_train)
data_test_std=sc.transform(data_test)

from  sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svc=SVC(C=1,random_state=1,kernel='linear')
svc.fit(data_train_std,target_train)
y_pred=svc.predict(data_test_std)
print("Accurasy score:",accuracy_score(target_test,y_pred))



#تحلیل اماری

import pandas as pd
import matplotlib.pyplot as plt
train=pd.read_csv("train.csv")

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
train["date"]=le.fit_transform(train["date"])
train["weather"]=le.fit_transform(train["weather"])
cols=[col for col in train.columns if col not in ['weather']]
data=train[cols]
target=train['weather']

from sklearn.model_selection import train_test_split
data_train,data_test,target_train,target_test=train_test_split(data,target,train_size=0.7,test_size=0.3)
from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(data_train,target_train)
plt.plot(data_test,reg.predict(data_test),color="red",linewidth=3)
plt.show()
