# 2nd , do this ....first we did merge_csv.py  ...refer class 139 for doubts
import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

# Calculate the values of C, m and find the movies that have more votes than 
# 0.9 quantile of the movie, just like how we did in Google Colab
C = df['vote_average'].mean() # C - Mean votes across the whole report
m = df['vote_count'].quantile(0.9) # m - The minimum votes required to be 
#listed in the chart.We can take the 90th Percentile as our cutoff. 
# In other words, for a movieto feature in the charts, it must have more 
# votes than at least 90% of the rest of the movies in the list.
q_movies = df.copy().loc[df['vote_count'] >= m] # we are copying only the data 
# which is >= m from df in q_movies 
# .loc filters from df only the data with vote_count >=m

# IMDB has created a formula known as weighted rating and it is famously used 
# in the industry  to get a score for their products/items
# It is  ((v/(v+m))*R)+((m/(v+m))*C)
# v - The number of votes for the movies (or number of ratings/reviews in 
# case of anamazon product)
# m - The minimum votes required to be listed in the chart
# R - Average rating of the movie
# C - Mean votes across the whole report
def weighted_rating(x, m=m, C=C): # x is the data of q_movies chk line 34
    v = x['vote_count'] # from q_movies take only teh 'vote_count'
    R = x['vote_average'] # from q_movies take only teh 'vote_average'
    return (v/(v+m) * R) + (m/(m+v) * C)
# Define a function to calculate the weighted rating (ie the score)and create 
# a new column of score (which we get as the result of the calculation 
# from formula in the function) in the dataframe for all the movies. Create a variable with
# top 20 movies as a list.
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
# The apply() method allows you to apply a function along one of the axis
# of the DataFrame (we are considering rows), In order to apply a function
#  to every row, you should use axis=1 param to apply().

q_movies = q_movies.sort_values('score', ascending=False) # we are now 
# sorting the movies in ascending order based on the scores

# Create a variable output with top 20 movies as a list with all the fields mentioned below.
output = q_movies[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()

# Now do content_filtering.py