#10 movies with highest number of votes
import pandas  as pd
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
print(fandango.nlargest(10,['VOTES']))