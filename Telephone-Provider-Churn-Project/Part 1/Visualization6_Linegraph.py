#Plotting Churn %
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
churned=df[df['Churn']=='Yes']['tenure']
not_churned=df[df['Churn']=='No']['tenure']
churned=churned.value_counts()
not_churned=not_churned.value_counts()
churn_percentage=100*churned/(churned+not_churned)
print(churn_percentage)
churn_percentage.plot()


