#Cleaned data frame without any movies havingg 0 votes
import pandas  as pd
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
fandango=fandango[fandango['VOTES']!=0]
print(fandango.head())