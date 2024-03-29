# -*- coding: utf-8 -*-
"""Python - String .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L34EKn50PUJ6ptTtDF-Vg64Q_vpeMjNv

**Intialize a string**
"""

#print multiple lines

s="""
      jquery exercise
      Javascript tutorrial
      Python Tutorial"""

print(s)

s1 =" JQuery Exercise\n Javascript Tutorial \n Python Tutorial"

print(s1)

"""**Access character from string**"""

a="Python String"
print(a)

b=a[2]
print(b)

b1=a[4+3]
print(b1)

b2=a[-1]
print(b2)

b3=a[-2]
print(b3)

"""**Python Strings are immutable**

--> Python strings are "immutable" which means they cannot be changed after they are created.

-->Therefore we cannot use [] operators on the left side of an assignment

-->we can create a new string that is a variation of the original.
"""

a="Python"

b="x"+a[1:]
print(b)

print(a)

"""**Python String concatenation**"""

a="Python" + " String"
print(a)

b1="Java"
b2=" sDeveloper"

b1+=b2
print(b1)

#"*" operator

a1="Python"+" String"
b3="< "+ a1*2 +" >"
print(b3)

"""**String Length**"""

a="Python String"
len(a)
a[12]

"""***Traverse string with while or for loop***

--> A lot of computations involve processing a string character by character at a time.

-->They start at the beginning select each character in turn do somethig to it and continue until the end.

--> this pattern of processing is called a traversal.

-->one can traverse a string with while or for loop.
"""

a="string"

i=0

while i <len(a):
  c=a[i]
  print(c)
  i=i+1

"""*** for loop**"""

a="python"
i=0

new=" "

for i in range(0,len(a)):

  b=a[i]

  new= new+b
  i=i+1

  print(b)

  print(new)

"""***string slices***

-->A segment of a string is called a "Slice". The slice syntax is used to get sub part of a string.

--> The slice s[start:end] is the element begininning at the
start(p) and extending up to but not including end(q).

--> The operator[p:q] return the part of the string from the pth character including the fist but excluding the last.

--> If we omit the 1st index(before the colon) the slice starts at the begininng of the string.

--> If you omit the 2nd indxed the slice goes to the end of the string.

--> If the first index is > than or equal to second the result is an empty. string represented by two quatation marks.

"""

s="Python"

print(s[0:4])

print("-------")

print(s[1:])

print("-------")

print(s[:])

print("-------")

print(s[1:100])

print("---------------------")

print(s[-1])

print("------")

print(s[-4])

print("-------")

print(s[:-3])

print("--------")

print(s[-3:])