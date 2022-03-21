#Finding how many movies does fandango have per year
import pandas  as pd

def get_year(film_name):
    return film_name[-5:-1]
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
fandango['YEAR']=fandango['FILM'].apply(get_year)
print(fandango['YEAR'].value_counts())
#Almost 95% of movies are from 2015