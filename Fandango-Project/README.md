Overview:
Several online sites provide reviews and ratings for movies that are released. Some of them sell tickets along with providing these ratings. The goal of this project is to check if one such site(www.fandango.com) is artificially boosting up ratings of movies so that their tickets get sold more often through data visualizations. Part 1 of this project will explore how fandango's stars displayed in their page corresponds to their actual rating. Part 2 will pit these fandango ratings against ratings by other sites.

Datasets used:

There are 2 main datasets used in this project. The first dataset has the ratings and score provided by fandango for movies released in mostly 2015. The second dataset contains ratings and scores provided by other sites(Rotten Tomatoes, Metacritic and IMDB). The main idea is to compare between the ratings provided by Fandango and other sites so as to conclude whether Fandango is actually rating movies higher so that their tickets gets sold easily.

Conclusion:

It has been viewed and verified through visualizations that Fandango is indeed rating movies higher so that their ticket sales are not affected by the movie ratings. Additionally, Fandango's own stars provided are greater than their actual ratings in many cases. This discrepancy can be forgiven as fractional ratings are difficult to be represented using stars and are sometimes rounded.Still, Fandango seems not to be harsh on movies that are rated low on other sites.

How to download and run the project:

1.Download the entire project.
2.Run each file to view visualizations.
3.Before running the file make sure that the correct filepath is provided while importing the dataset in code.
In each file, the statement for importing the dataset is present.
This statement is of the form - 
pd.read_csv(r'filepath/datasetname.csv')
Here filepath should be the actual filepath where you have downloaded and stored the dataset.
