# -*- coding: utf-8 -*-
"""Project 1- Python Quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yZlUPa4KadsIdJBBo6-btdlr2sjf5e01
"""

print("Welcome to my Project-1 Python quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score=0

answer=input("Python's name is inspired by.....? ")

if answer.lower()=="monty python":
  print("Correct!!!")
  score+=1
else:
  print("Wrong answer!!!")

answer=input("Python does not need a.....? ")

if answer.lower()=="compiler":
  print("Correct!!!")
  score+=1
else:
  print("Wrong answer!!!")

answer=input("The first python version released in .....? ")

if answer.lower()=="1991":
  print("Correct!!!")
  score+=1
else:
  print("Wrong answer!!!")

answer=input("Is python interpreted language.....? ")

if answer.lower()=="yes":
  print("Correct!!!")
  score+=1
else:
  print("Wrong answer!!!")

answer=input("Is python open source language.....? ")

if answer.lower()=="yes":
  print("Correct!!!")
  score+=1
else:
  print("Wrong answer!!!")


print("You got " + str(score) + " out of 5")
print("Percentage : " +str((score/5)*100)+ " %.")