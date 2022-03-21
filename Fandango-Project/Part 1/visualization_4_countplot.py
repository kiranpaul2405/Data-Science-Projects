#count plot for star difference
import pandas  as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
fandango=fandango[fandango['VOTES']!=0]
fandango['STARS_DIFFERENCE']=np.round(np.abs(fandango['RATING']-fandango['STARS']),1)
plt.figure(figsize=(12,5),dpi=120)
sns.countplot(data=fandango,x='STARS_DIFFERENCE',palette='magma')