#!/usr/bin/env python
# coding: utf-8

# ### 👨‍💻 Day 3 of 100DaysofPythonCode 🐍
#     - Randomization 
#     - Module 
#     - Data Structure (List, Nested Lists)
#     - IndexError

# In[2]:


import random

random_int = random.randint(1, 10) # generate random number btw 1 - 10 with both included
print(random_int)


# generating random floating point numbers
random_float = random.random()
print(random_float)

# love score 
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")


# ##### VIRTUAL COIN TOSS

# In[15]:


import random 

rand_side = random.randint(0, 1)
print(rand_side)
if rand_side == 1:
    print("Head")
elif rand_side == 0:
    print("Tail")


# In[33]:


# List 🇳🇬
ng_states = ["Lagos", "Abeokuta", "Abuja", "Borno", "Oyo"]
print(f"The Capital of Nigeria is {ng_states[0]}.")

ng_states = ng_states.extend(["Sokoto", "Ekiti", "Rivers"]) # add items to a list


# #### BANKER ROULETTE

# In[22]:


import random

name_str = input("Give the names of your friends.")
names  = name_str.split(",")

random_name = random.randint(0, len(names) - 1)
rand_choice = names[random_name]

print(f"{rand_choice} is gooing to buy the meal today!")


# In[34]:


row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to keep the treasure?")

vertical = int(position[1])
horizontal = int(position[0])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# #### Rock-Paper-Scissors

# In[34]:


import random

rock = """
  _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\

"""

paper = """
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
"""

scissors = """

  _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
"""

img_choice = [rock, paper, scissors]
message = int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if message >= 3 or message < 0:
    print("You typed an invalid number, you lose!")
else:
    print(img_choice[message])

rand_choice = random.randint(0, 2)

print(f"Computer chose:\n ")
print(img_choice[rand_choice])  
if message == 0 and rand_choice == 2:
    print("You win!")

elif message == 2 and rand_choice == 1:
    print("You win!")
elif message == 1 and rand_choice == 0:
    print("You win!")
elif message == 2 and rand_choice == 0:
    print("You lose!")
elif message == rand_choice:
    print("It's a Draw")
else:
    print("You lose!")

         
   


# In[ ]:





# In[ ]:




