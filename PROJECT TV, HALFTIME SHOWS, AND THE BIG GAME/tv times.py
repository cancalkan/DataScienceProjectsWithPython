#Hey There I am  Can Calkan.And it is my datacamp Tv, Half Time Shows learning project
#imports
import pandas as pd
import seaborn as sns
from IPython.core.display import display
from matplotlib import pyplot as plt

#importing my Csv files
super_bowls= pd.read_csv('datasets/super_bowls.csv')
tv= pd.read_csv('datasets/tv.csv')
halftime_musicians =pd.read_csv('datasets/halftime_musicians.csv')
#display first five rows
display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())
# Summary of the TV data to inspect
tv.info()
print('\n')
# Summary of the halftime musician data to inspect
halftime_musicians.info()
#%matplotlib inline (I commented it because I am using Pyhcharm not Jupyter Notebook )
plt.style.use('seaborn')
# Plot a histogram of combined points
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
display(super_bowls[super_bowls['combined_pts'] > 70])
display(super_bowls[super_bowls['combined_pts'] < 25])

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
display(super_bowls[super_bowls['difference_pts']==1])
display(super_bowls[super_bowls['difference_pts']>=35])

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)

#create a figure with 3x1 subplot and actvate the top sublplot
plt.subplot(3,1,1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Avarage Number of Us Viewers ')

#activate the middle subplot
plt.subplot(3,1,2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('HouseHold Rating')

#activate the bottom subplot
plt.subplot(3,1,3)
plt.plot(tv.super_bowl, tv.rating_household, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

#improve the spacing between subplots.
plt.tight_layout()
plt.show()
# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
display (halftime_musicians[halftime_musicians.super_bowl <= 27])

#count halftime show apperances for each musician and sort them for most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
display(halftime_appearances[halftime_appearances['super_bowl']>1])

# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance and display top 15 
no_bands= no_bands.sort_values('num_songs', ascending=False)
display(no_bands.head(15))

# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LII?
super_bowl_LII_winner = rams
print('The winner of Super Bowl LII will be the', super_bowl_LII_winner)
