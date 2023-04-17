
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("RF.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
   
    Age=request.args.get("Age")
    OverTime_Yes=request.args.get("OverTime_Yes")
    MonthlyIncome=request.args.get("MonthlyIncome")
    TotalWorkingYears=request.args.get("TotalWorkingYears")
    DailyRate=request.args.get("DailyRate")
    HourlyRate=request.args.get("HourlyRate")
    MonthlyRate=request.args.get("MonthlyRate")
    YearsAtCompany=request.args.get("TotalWorkingYears")
    prediction=classifier.predict([[Age,OverTime_Yes,MonthlyIncome,TotalWorkingYears,DailyRate,HourlyRate,MonthlyRate,YearsAtCompany]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    