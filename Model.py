import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

# User CGPA
def predicted_value(val):
    y_sample = np.array([val]).reshape(1,1)
    return lr.predict(y_sample)[0]

# Model Training
df = pd.read_csv(r'C:\Users\uduth\OneDrive\Desktop\Career\Projects and Case studies\CGPA Predictor\Dataset\placement.csv')
x = df.iloc[:,0:1]
y = df.iloc[:,1]

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

lr = LinearRegression()

lr.fit(X_train,y_train)
y_predict = lr.predict(X_test)


# UI Design
st.title('CGPA to Package Predictor')

cgpa = st.sidebar.number_input('Enter Your CGPA value')
btn = st.sidebar.button('Find Package')
if btn:
    try:
        if cgpa < 0 or cgpa > 10:
            st.error("CGPA should be between 0 and 10!")
        else:
            st.success('Submitted successfully')
            package = predicted_value(cgpa)
            st.write(f"Predicted Package: {package:.2f} LPA")
    except ValueError:
        st.error("Please enter a valid CGPA (numeric value)!")