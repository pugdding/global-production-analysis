#Import Libraries
import pandas as pd 
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 

#Looking For Datasets On Kaggle
dataset=pd.read_csv("globalPlasticProduction.csv")

#Print Head Values 
print(dataset.head())
print(dataset.dtypes)
print(dataset.shape)

#Question -- how has the annual growth rate changed of global plastic pollution changed overtime?

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




