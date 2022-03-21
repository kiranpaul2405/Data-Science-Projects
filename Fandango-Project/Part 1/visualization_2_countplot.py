#visualizing the count of movies per year with a count plot
import pandas  as pd
import seaborn as sns
def get_year(film_name):
    return film_name[-5:-1]
fandango=pd.read_csv(r'G:\Tech Topics\Data Science Course\06-Capstone-Project\fandango_scrape.csv')
fandango['YEAR']=fandango['FILM'].apply(get_year)

sns.countplot(data=fandango,x='YEAR')