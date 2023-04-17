import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


pickle_in = open("RF.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_attrition(Age,OverTime_Yes,MonthlyIncome,TotalWorkingYears,DailyRate,HourlyRate,MonthlyRate,YearsAtCompany):
    
   
    prediction=classifier.predict([[Age,OverTime_Yes,MonthlyIncome,TotalWorkingYears,DailyRate,HourlyRate,MonthlyRate,YearsAtCompany]])
    print(prediction)
    return prediction


def main():
      
    st.set_page_config(
        page_title="Predicting Employee Attrition",
        layout="wide",
    )
    image = Image.open('Banner.png')
    st.image(image)

    st.title("Predicting Employee Attrition")
    html_temp = """
    <div style="background-color:tomato;padding:0px">
    <h3 style="color:white;text-align:center;">Streamlit Predicting Employee Attrition ML Web App </h3>
    </div>

    """

    
    st.markdown(
        'Our app gives the best prediction about the attrition.')
    st.markdown(
        'Among all the 3 various Algorithms **Random Forest** has the best accuracy with 84.6%.')

   

    st.markdown(html_temp,unsafe_allow_html=True)
   
    Age = st.text_input("Age",placeholder="Enter the Age of Employee :")
   
    OverTime_Yes = st.text_input("OverTime_Yes",placeholder="If the Employee Works Overtime (1 or 0): ")

    MonthlyIncome = st.text_input("MonthlyIncome",placeholder="Enter the Monthly Income of the Employee : ")

    TotalWorkingYears = st.text_input("TotalWorkingYears",placeholder="Enter the total Working Years of the Employee : ")

    DailyRate = st.text_input("DailyRate",placeholder="Enter the Daily Working rate of the Employee :")

    HourlyRate = st.text_input("HourlyRate",placeholder="Enter the Hourly Working Rate of the Employee :")

    MonthlyRate = st.text_input("MonthlyRate",placeholder="Enter the Monthly Working Rate of the Employee :")

    YearsAtCompany = st.text_input("YearsAtCompany",placeholder="Enter the amonut of years employee worked at the Company : ")

    result=""
    if st.button("Predict"):
        result=predict_attrition(Age,OverTime_Yes,MonthlyIncome,TotalWorkingYears,DailyRate,HourlyRate,MonthlyRate,YearsAtCompany)

        if result == '1':
              st.success('Employee is Attrinated')
        else:
              st.success('Employee is Not Attrinated')
    

    if st.button("Click here to get Dataset"):
        with open('WA_Fn-UseC_-HR-Employee-Attrition.csv') as f:
            st.download_button('Download CSV', f, "WA_Fn-UseC_-HR-Employee-Attrition.csv")



if __name__=='__main__':
    main()
    
    
    