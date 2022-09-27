import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
# pd.set_option("display.max_rows", 5)

from learntools.core import binder

binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *

print("Setup complete.")

# Who are the most common wine reviewers in the dataset? 
# Create a Series whose index is the taster_twitter_handle category from the dataset,
# and whose values count how many reviews each person wrote.
reviews_written = reviews.groupby('taster_twitter_handle').size()
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# What is the best wine I can buy for a given amount of money? 
# Create a Series whose index is wine prices and whose values is 
# the maximum number of points a wine costing that much was given in a review. 
# Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).
best_rating = reviews.groupby('price').points.max()
best_rating_per_price = best_rating.sort_index()

# What are the minimum and maximum prices for each variety of wine? 
# Create a DataFrame whose index is the variety category from the dataset 
# and whose values are the min and max values thereof.
price_extremes = reviews.groupby('variety').price.agg([min, max])

# What are the most expensive wine varieties? Create a variable sorted_varieties containing
# a copy of the dataframe from the previous question where varieties are sorted in descending
# order based on minimum price, then on maximum price (to break ties).
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer.
# Hint: you will need the taster_name and points columns.
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
reviewer_mean_ratings.describe()  # to have a statistical summary and see if there are significant differences among reviewers

# What combination of countries and varieties are most common?
# Create a Series whose index is a MultiIndexof {country, variety} pairs.
# For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}.
# Sort the values in the Series in descending order based on wine count.
reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)  # size of every country-variety combination, sort_values does not require by, it will do it by size
