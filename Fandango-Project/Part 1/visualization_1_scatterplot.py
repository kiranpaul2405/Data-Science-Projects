#Basic scatterplot between movie ratings and votes it received on fandango website
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
plt.figure(figsize=(10,4),dpi=100)
sns.scatterplot(data=fandango,x='RATING',y='VOTES')