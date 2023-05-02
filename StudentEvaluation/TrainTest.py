import pandas as pd
import numpy as np

# import joblib
# LoadModel = joblib.load("Project_Model.pkl")

df = pd.read_csv("C:/Users/Saugat/Desktop/final year project/dataset.csv")

# print(df)

# sizes = df['Target'].value_counts(sort=1)
# print(sizes)

# Check info about all the columns 
# df.info() 





# df.drop(['GDP'], axis=1, inplace=True)
# print(df)

# df.iloc[df.Target == 'Graduate'] = 1
# df.iloc[df.Target == 'Dropout'] = 2
# df.iloc[df.Target == 'Enrolled'] = 3

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

# 34 ko thauma 34 hunxa hai
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
print(acc)




#User defined student data

Marital_status = 1
Application_mode = 6
Application_order = 1
Course = 11
Daytime_evening_attendance = 1
Previous_qualification = 1
Nationality = 1
Mother_qualification = 1
Father_qualification = 3

Mother_occupation = 4
Father_occupation = 4
Displaced = 1
Education = 0
Debtor = 0
Tution = 0
Gender = 1
scholarship = 0
Ageenrollment = 19
International = 0

Curricular_first_credited = 0
Curricular_first_enrolled = 6
Curricular_first_evaluation = 6
Curricular_first_approved = 6
Curricular_first_grade = 14
Curricular_first_withoutevaluations = 0

Curricular_first_credited = 0
Curricular_first_enrolled = 6
Curricular_first_evaluation = 6 
Curricular_first_approved = 6
Curricular_first_grade = 13.66667
Curricular_first_withoutevaluations = 0

Unemployment_rate = 13.9
Inflation = -0.3

GDP = 0.79



# User defined Prediction
z = model.predict([[Marital_status, Application_mode,
Application_order,
Course,
Daytime_evening_attendance, 
Previous_qualification,
Nationality,
Mother_qualification,
Father_qualification,

Mother_occupation,
Father_occupation,
Displaced,
Education,
Debtor,
Tution,
Gender,
scholarship,
Ageenrollment,
International,

Curricular_first_credited,
Curricular_first_enrolled,
Curricular_first_evaluation,
Curricular_first_approved,
Curricular_first_grade,
Curricular_first_withoutevaluations,

Curricular_first_credited,
Curricular_first_enrolled,
Curricular_first_evaluation,
Curricular_first_approved,
Curricular_first_grade,
Curricular_first_withoutevaluations,

Unemployment_rate,
Inflation,

GDP
]])

dict = ({
  0 : "Dropout",
  1 : "Enrolled",
  2 : "Graduate"
})

for value in z:
  output = dict[value]
  print("Output is:", output)

