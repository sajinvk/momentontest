
# coding: utf-8

# In[1]:


get_ipython().system('pwd')
# git clone https://github.com/momenton/momenton-code-test-movietweetings.git
get_ipython().system('ls *.dat')


# In[144]:


#!less movies.dat
import pandas as pd 
import numpy as np 
import re 
from datetime import datetime



# RAW DATA Import Soruce FIle : movies.dat
header = ["ID", "NAME_YEAR", "GENRE_LIST"]
movies_df=pd.read_csv('movies.dat',sep='::',engine='python',names=header)
#movies_df.head()
temp_df_1 = movies_df["NAME_YEAR"].str.split("(", n = 1, expand = True) 
temp_df_2= temp_df_1[1].str.split(")",n = 1 , expand = True) 
movies_df["NAME"] = temp_df_1 [0]
movies_df["YEAR"] = temp_df_2 [0]
#temp_df_2.head()
#movies_df.head()
movies_df.drop(columns =["NAME_YEAR"], inplace = True)
movies_df.head()

# Get unique list of All Genres
temp_df_3=movies_df["GENRE_LIST"].str.split("|", n = -1, expand = True)
#temp_df_3[7].unique()
arr = []
#for i in range(len(temp_df_3.columns) - 1 ):
#for i in range(1 ):
#arr.append(temp_df_3[0].dropna().unique)
unique_list = []    
#for val in arr:
#    if val not in unique_list: 
#            unique_list.append(val)
#print (unique_list) 

#temp_df_3.describe()
for i in range(len(temp_df_3.columns) - 1 ):
    x= list (set(temp_df_3[i].dropna()))
    for val in x:
           if val not in unique_list: 
                unique_list.append(val)
#print (type(x))
#print (unique_list)
df_unique_genre = pd.DataFrame(unique_list)
df_unique_genre.columns=['genre']
df_unique_genre


# In[136]:


#movies_df.head()
#movies_df_tmp1= movies_df["GENRE_LIST"].str.split("|", n = -1, expand = True)
#movies_df_tmp1.head()

df_movie_result = pd.concat([movies_df, movies_df_tmp1], axis=1)
df_movie_result.drop(columns =["GENRE_LIST"], inplace = True)


# In[137]:


df_movie_result.columns=['ID','NAME','YEAR','GENRE_0','GENRE_1','GENRE_2','GENRE_3','GENRE_4','GENRE_5','GENRE_6','GENRE_7']
df_movie_result.head(2)


# In[138]:


#DATAFRAME TO CSV 
df_unique_genre.to_csv('unique_genre.csv',header=True)
df_movie_result.to_csv('movie.csv',header=True)


# In[147]:


# Import USERS.dat 

header_users= ["userID", "twitter_id"]
user_df=pd.read_csv('users.dat',sep='::',engine='python',names=header_users)
#user_df

#IMPORT RATING.dat
header_rating = ["userID" , "movieID", "rating" ,"timestamp"]
rating_df =pd.read_csv('ratings.dat',sep='::',engine='python',names=header_rating)
#rating_df


# In[148]:


#DATAFRAME TO CSV 

# Movies to 2 CSV File 


#USERS and ratings TO 1 file 
user_df.to_csv('users.csv',header=True)
rating_df.to_csv('rating.csv', header=True)


# In[149]:


get_ipython().system('ls -l *.csv ')

