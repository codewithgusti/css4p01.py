#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 01:45:00 2024

@author: dianachapter
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movie_data_cleaned.csv',index_col=0)

print(df.corr())

correlation_plot =sns.heatmap(df.corr(), cmap="RdBu_r",annot=True, fmt=".2f", vmax=1, vmin=-1, square=True)

plt.show()


# # top 10 watched movies
# top_five_watched_movies = df.nlargest(5,'Rating')

# # Plotting a bar graph
# plt.figure(figsize=(6, 6))
# plt.bar(top_five_watched_movies['Title'],top_five_watched_movies['Rating'])
# plt.xlabel('Title of the Movie')
# plt.ylabel('Rating')
# plt.title('Top 10 Watched Movies Based on Ratings')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()

# # Show the plot
# plt.show()


