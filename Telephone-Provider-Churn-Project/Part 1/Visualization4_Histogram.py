#Histogram for distribution of tenure
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(15,12),dpi=200)
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
sns.displot(data=df,x='tenure',bins=60)