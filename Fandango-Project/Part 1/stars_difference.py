#New column for printing difference in no of stars and true rating
import pandas  as pd
import numpy as np
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
fandango=fandango[fandango['VOTES']!=0]
fandango['STARS_DIFFERENCE']=np.round(np.abs(fandango['RATING']-fandango['STARS']),1)
print(fandango.head())