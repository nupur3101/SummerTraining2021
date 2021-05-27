# Here we are creating Simple Machine Learning Model using SalaryData.csv

# Importing modules
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression


# Loading dataset 
dataset = pd.read_csv("SalaryData.csv")

# X -> Independent variable     y = Dependent variable
X = dataset['YearsExperience'].values.reshape(-1,1)    
y = dataset['Salary']


model = LinearRegression()
model.fit(X,y)                               # Creating model

# Storing the model in PredictSalary.pk1 file for future use
joblib.dump(model, 'PredictSalary.pk1')    

