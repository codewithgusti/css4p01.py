#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:43:40 2024

@author: dianachapter
"""

import pandas as pd


df = pd.read_csv('movie_dataset.csv')
df.columns = df.columns.str.replace(" ","")
df.dropna(thresh=5,axis=0)
df = df.reset_index(drop=True)

#The highest rated movie in the dataset?
highest_rated_movie = df[df['Rating'].max()==df['Rating']]
print(f'The highest rated movie is {highest_rated_movie}')
#The average revenue of all movies in the dataset?
avg_revenue = df['Revenue(Millions)'].mean()
print(avg_revenue)
#The average revenue of movies from 2015 to 2017 in the dataset?
filtered_revenue = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_filtered_revenue= filtered_revenue['Revenue(Millions)'].mean()
print(average_filtered_revenue)
#Movies that were released in the year 2016?
movies_released = df[df['Year']==2016].shape[0]
print(movies_released)
#Movies that were directed by Christopher Nolan?
directed_movies = len(df[df['Director']== 'Christopher Nolan'])
print(directed_movies)
#Movies in the dataset that have a rating of at least 8.0
rating_at_least_eight_point_zero = len(df[df['Rating'] >= 8.0])
print(rating_at_least_eight_point_zero)
#The median rating of movies directed by Christopher Nolan
median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
print(median_rating)
#The year with the highest average rating
average_rating_by_year = df.groupby('Year')['Rating'].mean().sort_values(ascending=False)
#the percentage increase in number of movies made between 2006 and 2016
percentage_increase = ((df[df['Year'] == 2016].shape[0] - df[df['Year'] == 2006].shape[0]) / df[df['Year'] == 2006].shape[0]) * 100
print(percentage_increase)
#Finding the most common actor in all the movies.
actors=df['Actors'].str.split(', ').explode()
actor_counts=actors.value_counts()
most_common_actor = actor_counts.idxmax()
print(most_common_actor)
#unique genres are there in the dataset.
genres = df['Genre'].str.split(', ').explode()
unique_genres_count =genres.nunique()
print(unique_genres_count)

df.to_csv("clean_data/movie_data_cleaned.csv")






