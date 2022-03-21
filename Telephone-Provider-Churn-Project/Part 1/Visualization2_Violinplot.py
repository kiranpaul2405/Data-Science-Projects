#Violin plot that shows distibution of TotalCharges
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
sns.violinplot(data=df,x='Churn',y='TotalCharges')