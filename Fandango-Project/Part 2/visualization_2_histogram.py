#Histogram showing rating differences
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
all_sites_rating=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\all_sites_scores.csv')
all_sites_rating['RATING_DIFFERENCE']=all_sites_rating['RottenTomatoes_User']-all_sites_rating['RottenTomatoes']
sns.histplot(data=all_sites_rating,x='RATING_DIFFERENCE',kde=True)