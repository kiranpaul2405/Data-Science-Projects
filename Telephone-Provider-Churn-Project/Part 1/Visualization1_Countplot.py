#Countplot to check for class imbalance
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
sns.countplot(data=df,x='Churn')