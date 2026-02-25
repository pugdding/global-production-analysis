#Import Libraries
import pandas as pd 
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 

#Import Scikit-Learn For Machine Learning
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 


#Looking For Datasets On Kaggle
dataset=pd.read_csv("globalPlasticProduction.csv")

#Print Head Values 
print(dataset.head())
print(dataset.dtypes)
print(dataset.shape)

#Question -- how has the annual growth rtate changed of global plastic pollution changed overtime?

#Analysis

#How To Calculate The Current Growth Rate 
annualGrowthRate=(dataset["Plastic"].pct_change() * 100)
dataset["annualGrowthRate"]=annualGrowthRate

#Graph
plt.figure()
sb.lineplot(data=dataset,x="Year",y="annualGrowthRate")

#Custom the Graph
plt.title("Annual Growh Rate Of Global Plastic Pollution")
plt.xlabel("Year")
plt.ylabel("Growth Rate By %")
plt.locator_params(axis="y", nbins=20)

#Create New Plot
plt.figure()
sb.lineplot(data=dataset, x="Year", y="Plastic")
plt.title("Global Plastic Pollution Per Year")
plt.xlabel("Year")
plt.ylabel("Blobal Plastic Pollution Per Million Tons")
plt.show()

#Introduction To Machine Learning 

#Get The Data 
x=dataset[["Year"]]
y=dataset[["Plastic"]]

#Split The Data Into Training and Testing 
xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.2,random_state=42)

#Creating The Model and Training
model=LinearRegression()
model.fit(xTrain,yTrain)
prediction=model.predict(xTest)

#Create The Chart
plt.figure()
plt.scatter(xTest, yTest, color="blue", label="Actual")
plt.plot(xTest, prediction, color="red", label="Predicted")
plt.title("Actual vs Predicted Plastic Production")
plt.xlabel("Year")
plt.ylabel("Plastic Production")
plt.legend()
plt.show()








