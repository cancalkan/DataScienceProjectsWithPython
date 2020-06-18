#This Project Provided By DataCamp.com Build By Can Calkan. I changed some of codes.
# Import modules
import pandas as pd 
from matplotlib import pyplot as plt 
# Read colors data
colors=pd.read_csv('datasets/colors.csv')
print(colors.head())

# How many distinct colors are available?
num_colors=str(colors.shape[0])
print("Number of Colors ="+num_colors)

# colors_summary: Distribution of colors based on transparency
colors_summary=(colors.groupby(colors['is_trans']).count())
print(+colors_summary)

# Read sets data as `sets`
#matplotlib inline(I DONT USE JUPYTERNOTEBOOK BECAUSE OF IT I COMMENTED)
sets=pd.read_csv('datasets/sets.csv')
print(sets.head())

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year=sets[['year', 'num_parts']].groupby('year',as_index=False).count()
# Plot trends in average number of parts by year
parts_by_year.plot(x='year', y='num_parts')
print(parts_by_year.head())

# themes_by_year: Number of themes shipped by year
themes_by_year= sets[['year','theme_id']].groupby('year', as_index=False).count()
print(themes_by_year.head())