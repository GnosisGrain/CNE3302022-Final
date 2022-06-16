#Simplified version of Python Dice Roll written by Markoni Ivanovic modified by Doc McDowell for Python 3.8
import random
roll_dice = input("Write start to dice roll: ")

if roll_dice == "start":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))
