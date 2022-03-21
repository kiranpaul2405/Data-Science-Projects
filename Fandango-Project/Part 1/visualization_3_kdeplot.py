#KDE plot for difference between user rating and stars shown
import pandas  as pd
import seaborn as sns
import matplotlib.pyplot as plt
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
fandango=fandango[fandango['VOTES']!=0]
plt.figure(figsize=(12,5),dpi=120)
sns.kdeplot(data=fandango,x='STARS',clip=[0,5],shade=True,label='True Rating')
sns.kdeplot(data=fandango,x='RATING',clip=[0,5],shade=True,label='Stars Displayed')
plt.legend(loc=(1.05,.5))