#No of movies with 0 votes
import pandas  as pd
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
print(len(fandango[fandango['VOTES']==0]))