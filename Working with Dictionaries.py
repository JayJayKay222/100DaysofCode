#!/usr/bin/env python
# coding: utf-8

# In[7]:


# sorting a dictionary by keys
best_teams = {'Real Madrid': 3, 'Chelsea':7, 'Liverpool':4, 'Man City':1, 'Barcelona':11,'Arsenal':21, 'PSG':5}

myKeys = list(best_teams.keys())
myKeys.sort()
myValues = list(best_teams.values())
myValues.sort()

sorted_teams = {i: best_teams[i] for i in myKeys}
print(sorted_teams)


# In[11]:


# merging two dictionaries

def bestTeams(best_teams, europe_best):
    return(europe_best.update(best_teams))

best_teams = {'Real Madrid': 3, 'Chelsea':7, 'Liverpool':4, 'Man City':1,
              'Barcelona':11,'Arsenal':21, 'PSG':5}
europe_best = {'Bayern':2, 'Ajax':23, 'BVB':13}

print(bestTeams(best_teams, europe_best))
print(europe_best)


# In[13]:


# remove duplicates words from a sentence
s = "Python is a great language and SQL is also great."
l = s.split()
k = []

for i in l:
    if (s.count(i) >= 1 and (i not in k)):
        k.append(i)
print(' '.join(k))        


# In[16]:


# convert string to dictionary
string = "Jan = January; Feb = Febuary; Mar = March; Apr = April"

dictionary = dict(subStr.split("=") for subStr in string.split(";"))
print(dictionary)


# In[ ]:




