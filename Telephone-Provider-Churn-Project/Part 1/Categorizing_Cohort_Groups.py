#Creating Cohort groups by using tenure
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def get_cohort_group(tenure):
    tenure=int(tenure)
    if(tenure<=12):
        return '0-12 Months'
    elif(tenure<=24):
        return '12-24 Months'
    elif(tenure<=48):
        return '24-48 Months'
    else:
        return 'Over 48 Months'
    
df=pd.read_csv('G:\Tech Topics\Data Science Course\DATA\Telco-Customer-Churn.csv')
df['Tenure Cohort']=df['tenure'].apply(get_cohort_group)
sns.scatterplot(data=df,x='MonthlyCharges',y='TotalCharges',hue='Tenure Cohort')