#new column for highlighting difference between RT critics and users and their mena
import numpy as np
import pandas as pd
all_sites_rating=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\all_sites_scores.csv')
all_sites_rating['RATING_DIFFERENCE']=np.abs(all_sites_rating['RottenTomatoes_User']-all_sites_rating['RottenTomatoes'])
print(all_sites_rating['RATING_DIFFERENCE'].mean())