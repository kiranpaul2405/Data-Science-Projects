import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
all_sites_rating=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\all_sites_scores.csv')
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
plt.figure(figsize=(12,5),dpi=150)
df=pd.merge(left=fandango,right=all_sites_rating,on='FILM',how='inner')
df['RT_Norm']=np.round(df['RottenTomatoes']/20,1)
df['RT_User_Norm']=np.round(df['RottenTomatoes_User']/20,1)
df['Meta_Norm']=np.round(df['Metacritic']/20,1)
df['Metacritic_User_Norm']=np.round(df['Metacritic_User']/2,1)
df['IMDB_Norm']=np.round(df['IMDB']/2,1)
norm_scores=df[['FILM', 'STARS', 'RATING','RT_Norm','RT_User_Norm', 'Meta_Norm', 'Metacritic_User_Norm', 'IMDB_Norm']]
sns.kdeplot(data=norm_scores,x='STARS',shade=True,label='STARS',clip=[0,5])
sns.kdeplot(data=norm_scores,x='RATING',shade=True,label='RATING',clip=[0,5])
sns.kdeplot(data=norm_scores,x='RT_Norm',shade=True,label='RT_Norm',clip=[0,5])
sns.kdeplot(data=norm_scores,x='RT_User_Norm',shade=True,label='RT_User_Norm',clip=[0,5])
sns.kdeplot(data=norm_scores,x='Meta_Norm',shade=True,label='Meta_Norm',clip=[0,5])
sns.kdeplot(data=norm_scores,x='Metacritic_User_Norm',shade=True,label='Meta_User_Norm',clip=[0,5])
sns.kdeplot(data=norm_scores,x='IMDB_Norm',shade=True,label='IMDB_Norm',clip=[0,5])
plt.legend(loc=(1.05,0.5))