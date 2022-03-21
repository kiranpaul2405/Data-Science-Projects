#Scatterplot for MonthlyCharges vs TotalCharges
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20,12),dpi=200)
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
sns.scatterplot(data=df,x='MonthlyCharges',y='TotalCharges',hue='Churn')