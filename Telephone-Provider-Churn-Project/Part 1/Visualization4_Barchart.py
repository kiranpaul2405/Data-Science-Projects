#Correlation value for features and barchart for the same
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
plt.figure(figsize=(15,8),dpi=250)
features_for_correlation=df[['gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod','Churn']]

features_for_correlation=pd.get_dummies(features_for_correlation)
correlation_with_churn=features_for_correlation.corr()['Churn_Yes']
df=pd.DataFrame(index=correlation_with_churn.index,columns=['Churn_Yes'],data=correlation_with_churn)
df=df.sort_values(by='Churn_Yes')
print(df)
sns.barplot(data=df,x=df.index,y=df['Churn_Yes'])

plt.xticks(rotation=90)