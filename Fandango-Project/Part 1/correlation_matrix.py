#Basic correlation matrix ----highlights on a slight discrepancy between stars and ratings
import pandas as pd
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
print(fandango.corr())