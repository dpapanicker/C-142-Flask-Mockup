import csv

all_movies = []

# UTF-8 is one of the most commonly used encodings, 
# and Python often defaults to using it. UTF stands for 
# “Unicode Transformation Format”, and the '8' means that 8-bit values
#  are used in the encoding.

#UTF-8 is a Unicode character encoding method. This means that UTF-8 
# takes the code point for a given Unicode character and translates 
# it into a string of binary. It also does the reverse, reading in 
# binary digits and converting them back to characters
with open('final.csv',encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []