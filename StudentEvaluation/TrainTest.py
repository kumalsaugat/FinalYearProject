import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Saugat/Desktop/final year project/dataset.csv")


df['Target'] = df['Target'].map({
    'Dropout':0,
    'Enrolled':1,
    'Graduate':2
})




# define dependent variable
y = df.iloc[:, 34].values

# y = df['Target'].values
y = y.astype('int64')





# define independent variable
# X = df.drop(labels=['Target'], axis=1)

X = df.iloc[:, 0:34].values  


# split data into train and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


#Select a model and Train It

from RandomForest import RandomForest

model = RandomForest()

model.fit(X_train, y_train)

#testing model

prediction_test = model.predict(X_test)


#For model Accuracy
acc =  accuracy(y_test, prediction_test)
print (acc)




