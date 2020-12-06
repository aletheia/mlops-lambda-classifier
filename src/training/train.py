# include numpy and pandas to handle linear algebra and dataset manipulation
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.metrics import confusion_matrix,classification_report

# Dataset has been downloaded and placed in the same folder of this notebook with name BankChurners.csv.
dataset_name = './BankChurners.csv'
df = pd.read_csv(dataset_name)
# Define a new dataset keeping only features that have a decent correlation with Attrition Flag, 
# which is representing churn
dfm = df[['Attrition_Flag', 'Total_Relationship_Count', 'Months_Inactive_12_mon',
          'Contacts_Count_12_mon', 'Total_Revolving_Bal', 'Total_Trans_Amt', 'Total_Trans_Ct',
          'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']]

x = dfm[['Total_Relationship_Count', 'Months_Inactive_12_mon', 'Contacts_Count_12_mon',
        'Total_Revolving_Bal', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1',
        'Avg_Utilization_Ratio']]
y = dfm['Attrition_Flag']

# Create training dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2)

# Model training
model = RandomForestClassifier(n_estimators=100, max_depth=13, random_state=2)
model.fit(x, y)
rfvalue = model.predict(x_test)

# print('Model Accuracy : ', accuracy_score(y_test, rfvalue) *  100)
# print('Model Recall : ', recall_score(y_test, rfvalue) *  100)
# print('Model Precision : ', precision_score(y_test, rfvalue) *  100)

# Save the model
import pickle
filename = 'trained_model.mdl'
pickle.dump(model, open(filename, 'wb'))