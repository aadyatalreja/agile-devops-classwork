# -*- coding: utf-8 -*-
"""LungCancerClassification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ddER_Q_wIiL-S_mMOZk-z_QDTfKJ0QMT
"""

# GaussianNB
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("lungcancer.csv")
print(df.head())

encoder = LabelEncoder()
df['GENDER'] = encoder.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])

x=df.drop('LUNG_CANCER',axis=1)
y=df['LUNG_CANCER']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
model=GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)

#printing the result of the model
NB_result = model.score(x_test, y_test)
print("Accuracy - test set: %.2f%%" % (NB_result*100.0))

# Decision Tree
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("lungcancer.csv")
print(df.head())

encoder = LabelEncoder()
df['GENDER'] = encoder.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])

x=df.drop('LUNG_CANCER',axis=1)
y=df['LUNG_CANCER']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model=DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)

#printing the result of the model
DT_result = model.score(x_test, y_test)
print("Accuracy - test set: %.2f%%" % (DT_result*100.0))

# Support Vector Machine
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("lungcancer.csv")
print(df.head())

encoder = LabelEncoder()
df['GENDER'] = encoder.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])

x=df.drop('LUNG_CANCER',axis=1)
y=df['LUNG_CANCER']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
model=SVC(kernel = 'linear', random_state = 0)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)


#printing the result of the model
SVM_result = model.score(x_test, y_test)
print("Accuracy - test set: %.2f%%" % (SVM_result*100.0))

# Random Forest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("lungcancer.csv")
print(df.head())

encoder = LabelEncoder()
df['GENDER'] = encoder.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])

x=df.drop('LUNG_CANCER',axis=1)
y=df['LUNG_CANCER']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model=RandomForestClassifier(n_estimators=100)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)

#printing the result of the model
RF_result = model.score(x_test, y_test)
print("Accuracy - test set: %.2f%%" % (RF_result*100.0))

# Logistic Regression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("lungcancer.csv")
print(df.head())

encoder = LabelEncoder()
df['GENDER'] = encoder.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])

x=df.drop('LUNG_CANCER',axis=1)
y=df['LUNG_CANCER']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)

#printing the result of the model
LR_result = model.score(x_test, y_test)
print("Accuracy - test set: %.2f%%" % (LR_result*100.0))

# KNN
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("lungcancer.csv")
print(df.head())

encoder = LabelEncoder()
df['GENDER'] = encoder.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])

x=df.drop('LUNG_CANCER',axis=1)
y=df['LUNG_CANCER']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(y_pred)

#printing the result of the model
KNN_result = model.score(x_test, y_test)
print("Accuracy - test set: %.2f%%" % (KNN_result*100.0))

y_plot=[NB_result,DT_result,RF_result,SVM_result,KNN_result,LR_result]
X_plot=['NB','DT','RF','SVM','KNN','LR']

plt.plot(X_plot, y_plot, 'o', color='blue')  # 'o' denotes points
plt.plot(X_plot, y_plot)
plt.grid(True)
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.show()
