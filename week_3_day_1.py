# # Week3
# # This week we will work on :
# # Working With Strings


# # 1.   Working With Numbers
# # 2.   Getting Input From Users




# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game




































# # Review
# create variable for the following :
# 1. age #integer variable
age= 28
# 2. name #string variable that has quotation marks
name = "Viviana"
# 3. song string vavariable
song = "imitadora"
# 4. food string variable
food = "Burger King"
# 5. number integer variable
number = 1906


# #now include the variables you just made print in the following...
#concatnation ------ + around your variables
#IF YOU INCLUDE A DIFFERENT TYPE OF VARIABLE IN CONCATNATION IT WON'T WORK
#print ("Once upon a time, there was a" + str(age) + "an old coder named" + name + ".")
#print ("there was a number " + str(number) + "as well")
#put the age in a new sentence 


#put the age and number in a new thing
date_of_birth =2021
number2= 123
number3 = 123.456
number4 = 123.33
number5 = 4555
#print (f"the date of birth is {date_of_birth} and his social security number is {number2} , {number3} , {number4}, and {number5}")


# Once upon a time, there was a [age] old coder named [name].


# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
#print (f"{name} liked to hum to the song {song} while coding. It was so annoying that their teamates would throw {food} until {name} would stop singing")

# Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
##########################################################################################


















##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"


# Here are some exercises to practice the rules:


# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# first_name
# last_name
# email_address
# percent
# variable_name
# zero
# list
#key word in python, you can't use it for your own variable names
# Creating Valid Names: Create valid names for the following descriptions:


# The first name of a person
# The last name of a person
# The email address of a person
# The percentage of marks obtained by a student
# A variable to store the number of items in a shopping cart




# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# first_name 
# lastName 
# email_address
# percentage
# variable_name
# one_variable
# email_address
# percentage
# ice_cream



############################################################################################


# # **Working with** **numbers** **bold text**
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


##########################################################################################
# #addition
#print (2+1)
# #multiplication
#print (2*2)
# #division
#print (6/2)
# #modulo
#print (7%4) #remainder of 7 divided by 4
# #powers
#print (2**3) #2 to the power of 3
# #get the max and min of a number
#print ("the max of 2 and 3 is " ,max (2,3))
#max means the highest number
#min means the lowest number
#print ("the min of 2 and 3 is " ,min (2,3))
# #round a number
#print ("round 3.9 is" ,round (3.9))
# # absolute value
#absolute value means the distance from 0
#print ("the absolute value of -3 is " , absolute value (-3))
# # order of operations aka PEMDAS
# print ("2 + 10 * 10 +3 is ", 2 + 10 * 10 +3 )

# #to do more you need to import special math libraries from python
#from math import    
# #this goes out and grabs some different math functions we can use
# #floor method ()
#print ("the floor of 3.7 is ",floor (3.7))
# #ceil method
#print ("the ceil of 3.7 is", ceil (3.7))
#print ("the ceil of 11.7 is", ceil (11.7))
# #sqrt method

#WILL NOT WORK UNLESS YOU IMPORT THE SPECIAL MATH LIBRARIES













##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
name= input ("what is your name?")
print ("hello", name)
# # basic math calculator
# #ask the user for 2 numbers
num1 = int (input ("enter a number") )
num2= int (input ("enter another number")) 
# # print out a statement where you:
# # add them together
print (num1 + num2)
# #multiply
print (num1 * num2)
# # find the max number
print (min (num1, num2))
# # find the remainder of the numbers
print (num1 % num2)
# #round one number
print (round (num1))








##########################################################################################
# # mad libs game
# print("Roses are {color}")
# print("{plural noun} are blue")
# print("I love {celebrity}")
# # On to codehs.com







