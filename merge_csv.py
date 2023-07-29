# first do this
import csv

# read movies.csv and separate out the headers and the data.
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

# adding a new variable poster_link in the header
headers.append("poster_link")
# create a new csvfile wehre we append the new header to this csv
with open("final.csv", "a+") as f: # a attribute means append
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_links.csv") as f:
    # # now read the contents of the movie’s poster links and store it in a variable.
    reader = csv.reader(f) 
    data = list(reader)
    all_movie_links = data[1:] # contains the links of all movies except some whch are missing

# we are first iterating over all the movie data that we have 
# which we have taken from movies.csv in the start.
for movie_item in all_movies:
    # movie_item[8] is the original_title header in movies.csv
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]: #movie_link_item[0] contains names of movies from movie_links.csv
                movie_item.append(movie_link_item[1]) #movie_item is the link pointing to all_movies. movie_link_item[1] is the link of the movie in movie_links.csv
                if len(movie_item) == 28: # we are also checking if the total length is 28 or not. Ideally,we should have 28 columns. If the number of columns is not 28, we are not adding the movie’s data.
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)

# line 28 - checking if there is any row in the movie’s poster link data
# that contains the name of the movie with the any() function. This will
# simply return True or False .movie_item[8] points to original_title in movies.csv

# now do the demographic_filtering.py and use the new created file ie final.csv