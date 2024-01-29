#!/usr/bin/env python
# coding: utf-8

# In[2]:


# iterate over a set 
test_set = set("python 3")
for val in test_set:
    print(val)


# In[3]:


# remove items from a set using pop()
def Remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)
        
initial_set = set([2,3,6,13,25,11,7,9])        
Remove(initial_set)


# In[5]:


# get common elements in a list 

def common(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result

a = [4,6,10, 22, 13, 20]
b = [22, 13 , 4, 2, 17, 19]

print(common(a,b))

a = [24,6,10, 21, 13, 20]
b = [22, 14 , 4, 2, 17, 19]
print(common(a,b))


# In[6]:


# convert set to a list
def conversion(a):
    return [el for el in a]
a = {2,6,12,7}
print(conversion(a))


# In[7]:


# intersection between two sets
def Intersection(list1, list2):
    list3 = [val for val in list1 if val in list2]
    return list3
a = [4,6,10, 22, 13, 20]
b = [22, 13 , 4, 2, 17, 19]
print(Intersection(a,b))


# In[ ]:




