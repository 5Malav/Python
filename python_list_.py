# -*- coding: utf-8 -*-
"""Python - List .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e89C03p6nOecLecJLkpAuhLmqFsHAPaP

**List**
--> A list a container which holds comma-separated values(items ot elements between square brackets where items or elements neeed not all have the same types

-->in general we can define a list as an object that contains multiple data items or elements

--> the content of a list can be changed during program execution. the size of a list can also change during execution as elements are added or removed from it.

**create a list**
"""

list1=[1,2,3,4]
print(list1)

list2=["red","blue","green","black"]
print(list2)

ls3=["red",1,2,3]
print(ls3)

ls4=[]
print(ls4)

#use of + operator
ls5=["white","yellow"]
ls6=["red","blue"]

ls7=ls5+ls6
print(ls7)

number=[1,2,3]
print(number[0]*4)

print(number*3)

"""**List Indices**

-->list indices works the same way string indices,list indices start at 0

--> if an index has a positive value it counts from the beginning and similarly it counts backwards if the index has a negative value.

-->as positive integers are used to index from the left end and negative integeers are used ti index from the right end so every item of a list gives two alternatives indices.
"""

ls=["red","blue","green","black"]
print(ls)
#indices start at 0 and end at 3

print(ls[0])

#print the first and last element of the list
print(ls[0],ls[3])

#return the last element

print(ls[-1])

"""**Add an item to the end of the list**"""

color_list=["red","green","blue","black"]
color_list.append("yellow")

print(color_list)

"""**Insert an item at a given position**"""

color_list=["red","green","blue","black"]

color_list.insert(2,"yellow")

print(color_list)

"""**Modify an list by using the index of an elemnent**"""

color_list=["red","blue","green","black"]
print(color_list)

color_list[1]="yellow"

print(color_list)

"""**remove and item from the list**"""

color_list=["red","black","blue","yellow"]

color_list.remove("yellow")

print(color_list)

"""**remove all the items from the list**"""

color_list=["red","blue","green","yellow"]

color_list.clear()

print(color_list)

"""**List slices**

-->List can be sliced like strings and other sequences.

--> sliced_list=List_name[start_index:end_index]

--> this refer to the items of a list starting at index start_index and stopping just before index end_index

--> the default value for its are 0(start_index) and the end(end_index) of the list. If you omit both indices the slice makes a copy of the original list.
"""

color_list=["red","blue","yellow","green"]

print(color_list[0:2])
#indices start at 0 and end at 1. it will not include 3rd item in the list

color_list=["red","blue","yellow","green"]

print(color_list[1:2])

print(color_list[1:-2])

print(color_list[1:-1])

color_list=["red","green","blue","yellow"]

print(color_list[:3])
#will include 1st 3 items and will ommit 4th item

color_list=["red","green","yellow","blue"]
print(color_list[:])

"""**Remove the item at the given position in the list and return it.**"""

color_list=["red","blue","green","yellow"]

color_list.pop(1)
#will remove "blue"
print(color_list)

"""**Return the index in the list of first item whose value is x**"""

color_list=["red","blue","green","yellow"]

print(color_list.index("red"))

print(color_list.index("yellow"))

"""**Return the number of times items appear in the list**"""

color_list=['red','red','red','green','green','yellow']

print(color_list.count('red'))

print(color_list.count('green'))

"""**Sort the items of the list in place**"""

color_list=['red','blue','green','black']

color_list.sort(key=None,reverse=False)
print(color_list)

color_list=['red','blue','green','black']
color_list.sort(key=None,reverse=True)
print(color_list)

"""**Return shallow copy of the list**"""

color_list=['red','green','blue','yellow','black']

color_list1=color_list.copy()
print(color_list1)

"""**List are mutable**

-->Items in the list are mutable i.e after creating a list you can change any items in the list
"""

color_list=['red','blue','green','yellow']
print(color_list)

color_list[1]='orange'

print(color_list)

"""**Convert list into tuple**"""

color_list=['red','blue','green','yellow']

tup=tuple(color_list)
print(tup)

"""** Use of double colone {::}**"""

listx=[1,2,3,4,5,6,7]

sublist=listx[0:6:2]
#listx[start:stop:step]

print(sublist)

sublist1=listx[::3]
#jump every 2 steps

print(sublist1)

sublist2=listx[6:2:-2]
#start from 7 then 2 jumps value will be 5
print(sublist2)

"""**Find the smallest and largest items in a list**"""

listx=[5,7,8,9,10,11,13,17,18,32]

print(min(listx))
print(max(listx))

"""**Compare two lists**"""

list_1=[1,2,3]
list_2=[4,5,6]
list_3=[1,4,5]
list_4=[1,2,3]

print(list_1==list_2)
print(list_2==list_3)
print(list_3==list_1)
print(list_1==list_4)

"""**Nested Lists**"""

listx=[["Malav","Joshi"],[1,2,3,4.1,5.1]]

print(listx[0][0])
print(listx[0][1])

listx.append([True,False])
print(listx)

#edit items in a list
listx[1][3]=4
print(listx)

listx[1][4]=5
print(listx)

"""**Get an index of an element**"""

listx=list("Malav Joshi")
print(listx)

print(listx.index("J"))

#define the index from which you want to search
print(listx.index("J",3))

#define the segment of the list to be searched
print(listx.index("o",5,9))

"""**Using lists as stacks**"""

color_list=['red','green','blue']
print(color_list)

color_list.append("yellow")
print(color_list)

color_list.append("black")
print(color_list)

color_list.pop()
print(color_list)

color_list.pop()
print(color_list)

"""**Using lists as Queues**"""

from collections import deque

color_list=deque(['red','blue','green'])
print(color_list)

color_list.append("yellow")
print(color_list)

color_list.append("black")
print(color_list)

color_list.popleft()
#1st element will be removed
print(color_list)

color_list.popleft()
print(color_list)