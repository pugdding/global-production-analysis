#import libraries 
import pandas as pd 
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 


#looking for datasets on Kaggle 
dataset=pd.read_csv("globalPlasticProduction.csv")

#print head values 
print(dataset.head())
print(dataset.dtypes())
print(dataset.shape())



#question -- how has the annual growth rate changed of global plastic pollution changed overtime?

#analysis 

#How To Calculate The Current Growth Rate 
annualGrowthRate=(dataset["Plastic"].pct_change() * 100)
dataset["annualGrowthRate"]=annualGrowthRate



#Graph
sb.lineplot(data=dataset,x="Year",y="annualGrowthRate")

#custom the graph
plt.title("Annual Growh Rate Of Global Plastic Pollution")
plt.xlabel("Year")
plt.ylabel("Growth Rate By %")
plt.locator_params(axis="y", nbins=20)
plt.show()



