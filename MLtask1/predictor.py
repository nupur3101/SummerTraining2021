# This is the file used for prediction by pre-trained model

# Importing modules
import joblib
import os

# Trained model is being loaded in 'model' variable
model = joblib.load('PredictSalary.pk1')      # PredictSalary.pk1 contains the trained model


os.system('clear')
os.system('tput setaf 6')

print("Salary Predictor".center(70,'*'))

os.system('tput setaf 7')

# Here we are taking input from user for years of experience
exp = float(input("\n\nEnter years of experience : "))

# 'predSal' variable contains the predicted Salary based on our ML model
predSal = model.predict([[exp]])

os.system('tput setaf 2')

print(f"\nPredicted Salary for {exp} years of experience : ",chr(8377),predSal[0])
print()
os.system('tput setaf 7')




