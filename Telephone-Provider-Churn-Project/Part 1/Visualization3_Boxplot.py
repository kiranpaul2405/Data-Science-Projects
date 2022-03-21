#Boxplot with total charges as per contract type along with churn as hue
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
plt.figure(figsize=(12,8),dpi=200)
sns.boxplot(data=df,x='Contract',y='TotalCharges',hue='Churn')
plt.legend(loc=(1.05,0.5))