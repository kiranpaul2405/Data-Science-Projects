import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
all_sites_rating=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\all_sites_scores.csv')
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
df=pd.merge(left=fandango,right=all_sites_rating,on='FILM',how='inner')
df['RT_Norm']=np.round(df['RottenTomatoes']/20,1)
df['RT_User_Norm']=np.round(df['RottenTomatoes_User']/20,1)
df['Meta_Norm']=np.round(df['Metacritic']/20,1)
df['Metacritic_User_Norm']=np.round(df['Metacritic_User']/2,1)
df['IMDB_Norm']=np.round(df['IMDB']/2,1)
norm_scores=df[[ 'STARS', 'RATING','RT_Norm','RT_User_Norm', 'Meta_Norm', 'Metacritic_User_Norm', 'IMDB_Norm']]
sns.clustermap(norm_scores,col_cluster=False)