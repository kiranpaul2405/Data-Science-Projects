#Basic data import and primary exploration
import pandas as pd
df=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
print(df.shape)
print(df.head(5))
print(df.columns)
print(df.describe())
print(df.info())