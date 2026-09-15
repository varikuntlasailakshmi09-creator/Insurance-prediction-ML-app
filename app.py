#step1 import models
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st
#this streamlit is for web based application project 

#web page code 
st.title("Healthy Insurance prediction")
img_url="https://cdn.zeebiz.com/sites/default/files/2026/03/09/401943-health-insurance.png"
st.image(img_url)

#LOAD DATA and ML MODEL PART  

#step2: load insurance data
url="https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df = pd.read_csv(url)

#step3: EDA: exploratory data analysis
df.drop("Customer_ID",axis = 1, inplace = True)

df['Previous_Insurance'] = df['Previous_Insurance'].map({'No':0,"Yes":1})
df['Insurance_Bought'] = df['Insurance_Bought'].map({'No':0,"Yes":1})

#Step4: divide dataset into features and target

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

#step 5: Divide data into training and testing part
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42, test_size=0.3)

#step6:Train Model
model=LogisticRegression()
model.fit(X_train,Y_train)

#show data sample
st.write(df.head())
#Create side bar for user input form

st.sidebar.title("Fill customer Details")
st.sidebar.image(img_url)

for index,col_name in enumerate(X.columns):
  min_v=X[col_name].min()
  max_v=X[col_name].max();
  if col_name!="previous_Insurance":
    value=st.sidebar.slider(f"Select value for{col_name}",
                            min_value=min_v,
                            max_value=max_v)
  else:
    value=st.sidebar.number_input(f"select value for {col_name}:")

 all_ans.append(value)
ud={j:all_ans[i] for i,j in enumerate(X.columns)}
user_df=pd.DataFrame(ud,index=[1])
st.write(user_df)

#*********************************prediction*************************
if st.button("Click to predict:"):
  with st.spinner("predicting..."):
    import time
    time.sleep(2)
    final_ans=model.predict([all_ans])[0]
  if final_ans==0:
     st.info(" ❎Customer will not Buy the Insurance❎")
  else:
    st.success("✅Customer will buy the Insurance ✅"")
               
