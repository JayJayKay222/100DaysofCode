#!/usr/bin/env python
# coding: utf-8

# #### PYTHON LIST

# In[2]:


# interchange first and last elements
def swapList(orgList):
    orgList[0], orgList[-1] = orgList[-1], orgList[0]
    return orgList

orgList = [23,3,42,12,16]
print(swapList(orgList))


# In[3]:


#swap elements in string list
test_list = ['thw', 'brst', 'is', 'yat', 'to' ,'comu']

rep = [sub.replace('w', 'e').replace('r','e').replace('a','e').replace('u','e')
      for sub in test_list]
print(str(rep))


# In[5]:


# check if element exists ina list

lst = [23,2,4,12,5,17]
i=2
if i in lst:
    print("2 exist in the list")
else:
    print("2 does not exist in the list")


# In[9]:


# cloning or copying a list using list comprehension

def Cloning(lsts):
    lst_copy = [i for i in lsts]
    return lst_copy

lsts = [13,2,4,12,5,17]
lst2 = Cloning(lsts)
print("List1: ",lsts)
print("List2: ", lst2)


# In[10]:


# odd numbers in a string
list1 = [13,2,4,12,5,17]

for num in list1:
    if num % 2 == 0:
        print(num)


# In[12]:


# remove multipl e empty spaces in a list
test_list = ['the', 'best', ' ', 'is', 'yet', ' ', 'to', 'come']
rep = list(filter(lambda x: x[0].lower() != x[0].upper(), test_list))
print(str(rep))

