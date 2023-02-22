#!/usr/bin/env python
# coding: utf-8

# In[53]:


"""
Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

"""
l1=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

a=lambda x : x[1]
for ele in range(0,len(l1)):
    print(a(l1[ele]))


# In[8]:


"""
Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(map(lambda x : x**2 , l))


# In[18]:


"""
Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions

"""
l2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tuple(map(lambda x : str(x) , l2))


# In[23]:


"""

Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.

"""
from functools import reduce
l3=list(range(1,25))
reduce(lambda x,y: x*y, l3)


# In[26]:


"""
Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.

"""

l3=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x : x%2==0 and x%3==0,l3))


# In[37]:


"""
Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']
"""

l4=['python', 'php', 'aba', 'radar', 'level']
list(filter(lambda x :  x[0]==x[len(x)-1] and  x[1]==x[len(x)-2],l4))


# In[ ]:




