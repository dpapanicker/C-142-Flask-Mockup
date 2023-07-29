# this is the 3rd program to do refer class 140 for doubts
# The general idea behind content based filtering is that if a person likes 
# a particular item, he or she will also like an item that is similar to it.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

# Remember, we do not have to do any sort of processing. We have already 
# exported this CSV which means that it already contains the metadata soup 
# string that we created. We can create a string that contains all the metadata 
# of a movie (info about keywords, actors, director and genres) and compare these 
# strings to find similarity between them.The more similar two strings are, the 
# more chances we have that the user will like that movie.That’s how content
# based filtering works and to find thissi milarity, we will be using the cosine
# similarity method!
# One thing that we now need to ensure is to drop the 
# rows that do not have a valid metadata soup string. We can do that with
#  the following code:
df = df[df['soup'].notna()] # The notna() method returns a DataFrame object
# where all the values are replaced with a Boolean value True for 
# NOT NA (not-a -number) values, and otherwise False.

count = CountVectorizer(stop_words='english')
# CountVectorizer converts a collection of text documents to a matrix 
# of token counts. stop_words{‘english’}, list, default=None If ‘english’,
#  a built-in stop word list for English is used like 'and,the,but.....'
count_matrix = count.fit_transform(df['soup']) # we are counting all the words
# after removing the stop words and then we are coverting it into a matrix or
# a 3d array (list of lists)

cosine_sim = cosine_similarity(count_matrix, count_matrix)
# Smaller angles between vectors produce larger cosine values, 
# indicating greater cosine similarity. For example: When two vectors 
# have the same orientation, the angle between them is 0, and the cosine
#  similarity is 1. Perpendicular vectors have a 90-degree angle between 
# them and a cosine similarity of 0.

# we want to change the index of our movie data to the name of the movies
df = df.reset_index() # The reset_index() method allows you reset the index 
#back to the default 0, 1, 2 etc indexes. By default this method will keep 
# the "old" idexes in a column named "index", to avoid this, use the drop 
# parameter.
indices = pd.Series(df.index, index=df['title']) # we are resetting our data for 
# df and then we are changing the index to the title of the movie.

# we will create the function that will get recommendations for us using
# our cosine_similarity classifier that we created earlier.
def get_recommendations(title,cosine_sim):
    idx = indices[title] # idx is storing the particular title passed 
    # in the get_recommendation function from the indices list created earlier
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].iloc[movie_indices].values.tolist()

# after this do main.py

# explanation of the above function get_recommendations from class 140 content filtering
#we are passing the title of the movie that the user likes and 
# our classifier. 
# We are then finding the index of the movie in our dataframe# using the 
# indices variable we created earlier, which contains the  indexes of all 
# the movies in the dataframe.We created this when we changed the index of 
# our dataframe to the title of the movie.
# we are creating a list of all the scores of the movies.This is the score
#  of similarity of each movie with what the user likes.
#  We are then  using the sorted function on our data to sort the scores of 
# all the movies and we are reversing its order with reverse=True attribute.
# We are then taking elements from 1:11. We are not starting with 0 since 
# the movie that the user likes will have the highest score (perfect score).
# We are then taking out the indexes of all the movies that we want to
# recommend and finally we are returning the titles of all the movies
# that our system recommends!



