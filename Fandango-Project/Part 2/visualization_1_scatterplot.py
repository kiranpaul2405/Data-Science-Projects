#Scatterplot for difference  between RT User and Critic scores
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.xlim(0,100)
plt.ylim(0,100)
plt.figure(dpi=150)
all_sites_rating=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\all_sites_scores.csv')
sns.scatterplot(data=all_sites_rating,x='RottenTomatoes',y='RottenTomatoes_User')
plt.show()