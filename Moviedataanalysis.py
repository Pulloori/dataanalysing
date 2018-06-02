
# coding: utf-8

# In[2]:


# Anlaysing and visualisation of IMDB-Movie-data set

import pandas as pp
from pandas import DataFrame as ff 
hh_ff = pp.read_csv('G:\Downloads\IMDB-MovieData.csv')
print(hh_ff.head())


# In[3]:


hh_ff.size


# In[4]:


# Converting set of Genres into set of Genre-strings to compare.. 
hh_ff['Genre_str'] = hh_ff['Genre'].str.split(',')
hh_ff.head()


# In[11]:


# how many times each genre occured!
Animation_ff = hh_ff[hh_ff.Genre_str.map(lambda x:'Animation'in x)]
print( 'No. of Animation movies-', len(Animation_ff.index))

Fantasy_ff = hh_ff[hh_ff.Genre_str.map(lambda x:'Fantasy'in x)]
print( 'No. of Fantasy movies-', len(Fantasy_ff.index)) 

Action_ff = hh_ff[hh_ff.Genre_str.map(lambda x:'Action'in x)]
print( 'No. of Action movies-', len(Action_ff.index)) 


# In[14]:


# Checking of set of genres in each movie
combo_lambda = lambda x: set(['Action','Adventure','Sci-Fi']).issubset(x)
combo_ff = hh_ff[hh_ff.Genre_str.map(combo_lambda)]
print ('No.of combo movies', len(combo_ff.index))
combo_ff


# In[15]:


#Genre_count
counter_lambda = lambda x: len(x)
hh_ff['Genre_count'] = hh_ff.Genre_str.apply(counter_lambda)
hh_ff.head()


# In[18]:


import matplotlib.pyplot as plt

plt.hist(hh_ff.Genre_count)
plt.title("Genres Histogram")
plt.xlabel(" Genres_count ")
plt.ylabel(" Movies ")
plt.axis([0, 9, 0, 1000])
plt.show()


# In[19]:


# Count of each genre
from collections import Counter

flat_Genre = [item for sublist in hh_ff.Genre_str for item in sublist]

Genre_diction = dict(Counter(flat_Genre))

print (Genre_diction)


# In[24]:


x = list(range(len(Genre_diction)))
plt.xticks(x, Genre_diction.keys(), rotation=90)
plt.bar(x, Genre_diction.values())
plt.title(" Genres Bargraph ")
plt.xlabel(" Genres ")
plt.ylabel(" No. of Movies ")
plt.grid()
plt.show()


# In[44]:


# different ratings
print ('Ratings', hh_ff.Rating.unique())


# In[29]:


# mean of all the ratings
import numpy as np
np.mean(hh_ff.Rating)


# In[30]:


# common Rating and how many times it is given..
from scipy import stats
stats.mode(hh_ff.Rating)


# In[32]:


plt.hist(hh_ff.Rating)
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5 ,6.0 ,6.5 ,7.0 ,7.5 ,8.0 ,8.5 ,9.0 ,10.0 ])
plt.title(" Rating Histogram ")
plt.xlabel('Rating') 
plt.ylabel('No.of movies')
plt.grid()
plt.show()


# In[33]:


# gives many values for each column
print(hh_ff.describe())


# In[56]:


# top rated movies
ratings_view = hh_ff[['Title','Rating','Year','Actors']]
ratings_view.groupby(['Title','Actors'], as_index=True).mean().sort_values(by=['Rating'], ascending=False).head(15)

