# print("Hello this is our first python program")
# name = "Harry"
# Age = 34
# Price = 89.0

# Arithmetic, Relational, Assignment or Logical operator
# a =10
# b=4
# sum = a + b
# diff = a - b
# div = a / b
# mul = a * b
# print(sum)
# print(diff)
# print(div)
# print(mul)
# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)

# num = 10
# num += 10
# print("Num: ", num)

# a=4
# b=5
# var1=True
# var2=False
# print("AND Operator: ", var1 and var2)
# print("OR Operator: ", var1 or var2)
# print("NOT Operator: ", var1 not var2)

#type conversin
# a =int("2")
# b=9.0
# print(a+b)

# Practice with input
# a = int(input("First Number= "))
# b = int(input("Second Number= "))
# print(a+b)

# print area of a square
# length = int(input("Enter Length= "))
# width = int(input("Enter Width= "))
# print("Area= ", length * width)


# print average of two float numbers
# a = int(input("Enter a= "))
# b = int(input("Enter b= "))
# print("Area= ", (a+b)/2)


# print greater of two  numbers
# a = int(input("Enter a= "))
# b = int(input("Enter b= "))
# print(a>=b)

# Strings
# str1 = "Hello"
# str2 = 'Hi'
# str3 = '''This is strings topic'''
# print(str1)
# print(str2)
# print(str3)

# str4 = "Hello how are you.\n are you ok" 
# str5 = "yes iam ok"
# finalstr = str4 + str5
# print(finalstr)


# Slicing = accessing parts of a string
# a = "Apple"
# print(a[1:4])
# print(a[-3:-1])
# print(a.endswith("le")) 
# print(a.capitalize())
# print(a.replace("A", "a"))
# print(a.find("A"))
# print(a.count("p"))


# practise qs
# # input form user and print its length
# a=input("Enter Word: ")
# print(len(a))

# find occurrence of $ in a string
# a="C++&&"
# print(a.count("&"))


#Conditional Statement
# age = 21
# if(age >= 18):
#     print("Y'll get license")

# light = "green"
# if(light == "red"):
#     print("stop!")
# elif(light == "green"):
#     print("go") 
# else:
#     print("Light is broken")    


# num=5
# if(num > 2):
#     print("greater than 2")
# if(num > 6):
#     print("greater than 3")       
    
    
    
# Grade students based on marks
# marks = int(input("Enter Student Marks: "))
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"       
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
    
# print("Grade of a Student -> ", grade) 


#Nesting = if within another if
# age = 95
# if(age >= 18):
#     if(age >= 80):
#         print("Cannot Drive")
#     else:
#         print("Can Drive")    


# WAP check number is even or odd
# num = int(input("Enter Number: "))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# WAP fint greatest of 3 numbers
# Find the greatest of 4 numbers

# num1 = 3
# num2 = 5
# num3 = 2
# num4 = 7

# if num1 >= num2 and num1 >= num3 and num1 >= num4:
#     print(num1)
# elif num2 >= num3 and num2 >= num4:
#     print(num2)
# elif num3 >= num4:
#     print(num3)
# else:
#     print(num4)
        


# WAP check number is a multiple of 7 or not
# num = int(input("Enter Number: "))
# if(num % 7 == 0):
#     print("Multiple of 7")
# else: 
#     print("Not Multiple")    
        
       
# Lists and Tuples
# Lists
'''string are immutable means not to ne changed
lists are mutable means to be changed'''
# marks= [32,43,56,75,54]  
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[4])

# students = ["Karan", 54, "Delhi"] 
# students[0] = "John" 
# print(students)
# print(students[1:2])

# List Methods
# numbers = [2,3,4,1]
# numbers.append(4) # adds to the last
# print(numbers) 
# print(numbers.sort()) # Assecending
# print(numbers)
# print(numbers.sort(reverse=True)) # Descending
# print(numbers)
# numbers.reverse() # reverse list
# print(numbers)
# numbers.insert(1,5)  # insert index
# print(numbers) 
# numbers.remove(1) # remove forst ocuurence
# print(numbers)
# numbers.pop(3) # remove elements at particular index
# print(numbers)


# Tuples create immutable sequences of values
# tup = (1,2,3,4)
# print(type(tup))
# print(tup[2])
# # tup[2]=4 # not allowed in tuples
# # Tuples Methods
# tup.index(2) # returns index of first occuerrence
# print(tup)
# tup.count(2) # counts total occurence
# print(tup)


# Practise qs
# WAP ask the user names of 3 favorite movies and store them in list
# mov1 = input("Enter 1st Movie: ")
# mov2 = input("Enter 2nd Movie: ")
# mov3 = input("Enter 3rd Movie: ")
# movies = []
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# WAP and checks if a list contains a palindrome of elements.
# list1 = ["Ma'am"]
# list2 = [1,2,3]
# copylist1 = list1.copy()
# copylist1.reverse()
# if(copylist1==list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome") 


# WAP count the number of stds with Grade A in the following tuple and store the values in a list and sort them from A to D
# Grades = ["C", "D", "A", "A", "B", "B", "A"]
# Grades.sort()
# print(Grades) 



# Dictionaries and Set
# Dictionaries to store data values in key:value pairs and it is mutable
# info = {
#     "Key" : "Value",
#     "Name" : "John",
#     "Learning" : "Coding",
#     "Age" : 35,
#     "Subjects" : ["Python", "C++", "Java"],
#     "Topics" : ("Dict", "Set")
# }
# info["Name"] = "Doe"
# print(info)


# Nested Dictionary
# student = {
#     "Name" : "John",
#     "Subjects" : {
#         "Maths" : 45,
#         "Physice" : 43,
#         "Chemistry" : 76
#     }
# }  
# print(student["Subjects"]["Chemistry"])
# print(student.keys()) # return all keys
# print(student.values()) # return values
# print(student.items()) # return pairs
# print(student.get("Name"))
# newdict = {"city" : "delhi"}
# student.update(newdict) # inserts the specified items to the dictionary
# print(student)


# Set collection of unordered items each element in set must be unique and immutable
'''ignores duplicate and repeated values'''
# collection = {1,2,3,4, "Hello World"}
# print(collection)
# print(type(collection))
# collection.add(5) # add value
# collection.add(5,3,4) # error
# print(collection)
# collection.remove(3) # remove value
# print(collection)
# collection.clear() # empties the set
# print(collection)
# collection.pop() # removes a random value
# print(collection)
# Set1 = {1,2,3,4}
# Set2 = {5,6,7,8}
# print(Set1.union(Set2))
# print(Set1)
# print(Set2)
# print(Set1.intersection(Set2))
# print(Set1)
# print(Set2)

# Lets Practice qs
# store following word meanings in a python dictionary
'''Cat : a small animal'''
'''Table : a piece of furniture, list of facts and figures'''
# dictionary = {
#     "Cat" : "a small animal",
#     "Table" : ["a piece of furniture", "list of facts and figures"]    
# }
# print(dictionary)



# you are given a list of subjects for students. assume one classroom is required for 1 subject. How many classrooms are needed by all students
# "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# subjects = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }
# print(subjects)
# print(len(subjects))

# WAP enter marks of 3 subjects from user and store them in a dictionary. Start with and empty dictionary and add one by one. use subject name as key and marks as value
# marks = {}
# a = int(input("Enter phy marks: "))
# marks.update({"Phy" : a})
# a = int(input("Enter chem marks: "))
# marks.update({"Chem" : a})
# a = int(input("Enter math marks: "))
# marks.update({"Math" : a})
# print(marks)


# figure out a way to store 9 and 9.0 as seperate values in set. you can take help of buit-in data types 
# values1 = {9, "9.0"}
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)

# Loops are uesd to repeat instructions
# while loops
# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1
    
# i=1
# while i<=5:
#     print("Pyhton")
#     i =+ 1 

# print numbers from 1 to 5
# i=5
# while i>=1:
#     print(i)
#     i-=1   


# Practice questions
# print numbers from 1 to 100
# count = 1
# while count <= 100:
#     print(count)
#     count += 1
    
# print numbers from 100 to 1
# count = 100
# while count >= 1:
#     print(count)
#     count -= 1    


# Print table of a number
# n=int(input("Enter Number: "))
# i = 1
# while i <= 10:
#     print(i*n)
#     i+=1

# print the elements of following list using a loop
# num = [1,4,9,16,25,36,49,64,81,100]
# heroes = ["ironman", "thor", "superman", "batman"]
# idx = 0
# while idx <= len(heroes):
#     print(heroes[idx])
#     idx+=1
    
    
# search for a number x in this tuple using loop
# num = (1,4,9,16,25,36,49,64,81,100)
# i=0
# x = int(input("Enter Number to Search: "))
# while i < len(num):
#     if(num[i]==x):
#         print("Found at Index: ", i)
#     i+=1   


# Break used to terminate the loop when wncountered
# Continue terminate execution in the current iteration & continues execution of the loop with the next iteration
# i=1
# while i<= 5:
#     print(i)
#     if 1==3:
#         break
    
# i=1
# while i<= 5:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1


# For loop used for sequential traversal list, string, tuples etc
# list = [1,2,3,4,5]
# for val in list:
#     print(val)
# tup = (1,2,3,4,5)
# for num in tup:
#     print(num)
# str = "Python"
# for char in str:
#     if char == "o":
#         print("O found")
#         break
#     print(char)

# Practice qs
# Print the elements of the following list using a loop
# list = [1,4,9,16,25,36,49,64,81,100]
# for num in list:
#     print(num)

# Search for a number x in this tuple using loop
# tup = (1,4,9,16,25,36,49,64,81,100)
# x=25
# idx=0
# for val in tup:
#     if (val==x):
#         print("Number found at idx: ", idx)
#     idx+=1  

# Range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# seq=range(5)
# for i in seq:
#     print(i)

# for i in range(5): #range(stop)
#     print(i)

# for i in range(2, 5): #range(start, stop)
#     print(i)

# for i in range(2, 5, 2): #range(start, stop, step means increase by 2)
#     print(i)

# even numbers
# for i in range(2, 10, 2):
#    print(i)
   
# odd numbers
# for i in range(1, 10, 2):
#     print(i)   

# print numbers from 1 to 100
# for i in range(100):
#     print(i)

# print numbers from 100 to 1
# for i in range(100, 0, -1):
#     print(i)

# print table of a number
# n = int(input("Enter Number: "))
# for i in range(1, 11):
#     print(i*n)


# Pass statement is a null statement that does nothing . it is used as a placeholder for future code
# for i in range(5):
#     pass

# qs
# WAP find sum of first n numbers(using while)
# n=5
# sum = 0
# i=1
# while i<= n:
# for i in range(1, n+1):
    # sum+=1
    # i+=1
# print("Total Sum: ", sum)




# WAP find the factorial fo first n numbers(using for)git add . && git commit -m "update" && git push origin main
# n=5
# fact = 1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("Total Factorail: ", fact)    

# n=5
# fact=1
# for i in range(1, n+1):
#     fact*=i
# print("Factorial is: ", fact)    


# Functions
# function definition
# def sum(a, b): # parameter
#     s=a+b
#     return s
# print(sum(2,3)) # function call, arguments
# print(sum(12,4))

# average of 3 numbers
# def average(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     return avg
# average(98, 97, 10)

# Built-in function like print(), len() etc
# user defined function
# defined by User

# default parameter
# def product(a=2,b=3):
#     print(a*b)
#     return a*b
# product()

# def product(a,b=3):
#     print(a*b)
#     return a*b
# product(3)

# 3 lets practice question
# WAP to print the length of a list. (list is the parameter)
# cities = ["delhi", "pune", "mumbai"]
# def printlen(list):
#     print(len(list))
# print(len(cities))    



# WAP to print the elements of a list in a single line. (list is the parameter)
# cities = ["delhi", "pune", "mumbai"]
# def printelement(list):
#     for item in list:
#         print(item, end=" ")
# printelement(cities)

# WAP to find the factorial of a n. (n is the parameter)
# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact*=1
#         print(fact)
# factorial(5)

        
    
# WAP to convert usd to inr
# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val, "USD =", inr_val, "INR")
# converter(2)   


# WAP to find even and odd
# def evnodd(n):
#     if(n%2==0):
#         print("Even Number ")
#     else:
#         print("Odd Number ") 
# n=int(input("Enter Any Number: "))
# evnodd(n)            



# Recursion = when a function calls iteslf repeatedly
# def show(n):
#     if(n==3):
#         return
#     print(n)
#     show(n-1)
# show(5)

# factorial
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))    


# Practice question
# Write a recursive function to calculate the sum of first n natural numbers.
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+n
# print(sum(3))    



# write a recursive function to print all elements in a list. Hint use list and index as parameter
# def printlist(list, index=0):
#     if(index==len(list)):
#         return
#     print(list[index])
#     printlist(list, index+1)
# fruits=["mango", "banana", "apple"]
# printlist(fruits) 
   
    
# File I/O  
# read mode 
# f=open("sample.txt", "r")  
# data=f.read()
# print(data)
# # print(type(data))
# # line1=f.readline()
# # print(line1)
# line2=f.readline()
# print(line2)
# f.close()


# write mode
# f=open("sample.txt", "a")
# f.write("\n After that next js")
# f.close()

#w+ mode
# f=open("sample.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()


#with
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# with open("sample.txt", "w") as f:
#     f.write("New Data")


# practice question
# create a new file example.txt using python. add the following data in it:
#     hi everyone
#     we are learning file i\o
#     using java
#     i like programming in java
# with open("sample.txt", "w")  as f:
#     f.write("hi everyone\nwe are learning file i\o\n")
#     f.write("using java\ni like programming in java")




#qs2 WAP that replace all occurrence of java with python in above file
# with open("sample.txt", "r")  as f:
#         data=f.read()
# newdata=data.replace("java", "python")
# print(newdata)
# with open("sample.txt", "w")  as f:
#         f.write(newdata)   



#qs3 search if "learning" word exist
# def checkword():
#     word="learningx"
#     with open("sample.txt", "r") as f:
#         data=f.read()
#         if(data.find(word)!=-1):
#             print("found")
#         else:
#             print("not found") 
# checkword()  


#qs4 WAP to find in which line of the file does the word "learning" occurs first print -1 if word not found
# def checkline():
#     word="learning"
#     data=True
#     lineno=1
#     with open("sample.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(lineno)
#             lineno+=1    
#     return -1
# checkline()





# qs5 from a file containig numbers separeted by comma, print the count of even numbers                 
# with open("sample.txt", "r") as f:
#     data = f.readline()
#     print(data)
# num=""
# for i in range(len(data)):
#     if(data[i]==","):
#         print(int(num))    
#         num=""
#     else:
#         num+=data[i]  

# alternative
# with open("sample.txt", "r") as f:
#     data = f.read()
#     count=0
#     nums=data.split(",")
#     for val in nums:
#         if(int(val)%2==0):
#             count+=1
#     print(count)  

# project 1 greetings
# name = input("Enter Your Name: ")
# print(f"Hello {name}. ")
# print("Welcome to the world of python")

# project 1 Band/Group name generator
# print("Welcome to the Band/Group Name Generator")
# color = input("What is your favorite color?")
# print(color)
# animal = input("What is your favorite animal?\n")
# print(animal)
# print(f"Your Band/Group name could be {color} {animal}. ")

# project 3 Gross Pay
# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")
# newhour = float(hours)
# newrate = float(rate)
# print(newhour*newrate)


# project 4 Celsius to Fahrenheit
#   celsius = input("Enter Temperature in Celsius: ")
#   newcelsius = float(celsius)
#   fahrenheit = (newcelsius * 9/5) + 32
#   print(fahrenheit)


# # project 5 Trip Cost Calculator
#    print("Welcome to the Trip Cost Calculator ")
#    days = int(input("Enter number of days: "))
#    cost = float(input("Enter cost per night: "))
#    flightcost = float(input("Enter flight cost: "))
#    carprice = float(input("If you need rental car enter 1 else 0: "))
#    otherexpense = float(input("Enter other expenses: "))
#    totalcost = round(days * cost + flightcost + days * carprice + otherexpense, 2)
#    print(f"Your total cost is {totalcost} ")

# print("Welcome to the Mortgage Calculator ")
# salary = int(input("What is your salary: "))
# if salary > 2000:
#     print("your are eligible for mortgage ")
#     creditscore=int(input("What is your credit score: "))
#     if creditscore > 800:
#         print("Interest Rate is 4% ")
#     else:
#         print("Interest Rate is 6%")    
# else:
#     print("You're not eligible for mortagage ")


# even odd program
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# chained conditions
# print("Welcome to the Mortgage Calculator ")
# salary = int(input("What is your salary: "))
# if salary > 2000:
#     print("your are eligible for mortgage ")
#     creditscore=int(input("What is your credit score: "))
#     if creditscore > 800:
#         print("Interest Rate is 4% ")
#     elif creditscore > 750:
#         print("Interest Rate is 8%")    
#     else:
#         print("Interest Rate is 6%")    
# else:
#     print



# Body Mass Index (BMI) Calculator
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in m: "))
# bmi=round(weight/height**2,2)
# if bmi < 18.5:
#     print("you are underweight.")
# elif bmi < 25:
#     print("you weight is normal.")
# elif bmi < 30:
#     print("you are overweight.")
# else:
#     print("you are obese.")            



# Multiple IF
# print("Welcome to the Mortgage Calculator")

# salary = int(input("What is your salary: "))

# if salary > 2000:
#     print("You are eligible for a mortgage.")
    
#     creditscore = int(input("What is your credit score: "))
    
#     if creditscore > 800:
#         rate = 4
#         print("Interest Rate is 4%")
#     elif creditscore > 750:
#         rate = 6
#         print("Interest Rate is 6%")
#     else:
#         rate = 8
#         print("Interest Rate is 8%")
    
#     disability = input("Do you have any disability? Y or N: ")
    
#     if disability.upper() == "Y":
#         rate -= 2
#         print("You are eligible for a 2% discount due to disability.")
    
#     print(f"Final Interest Rate: {rate}%")
# else:
#     print("Sorry, you are not eligible.")



# Burger Order Program
# print("Welcome to the Burger Shop! ")
# size = input("What size burger do you want? M, N or L ")
# addmushroom = input("Do you want mushroom? Y or N ")
# extrecheese = input("Do you want extra cheese? Y or N ")
# bill=0
# if size=="M":
#     bill+=5
# elif size=="N":
#     bill+=8
# else:
#     bill+=10    
    
# if addmushroom=="Y":
#     if size=="L":
#         bill+=2
#     else:
#         bill+=1
     
# if extrecheese == "Y":
#     bill+=1
    
# print(f"Your final bill is {bill}")         
                
        
# # with logical operator     
# # print("Welcome to the Mortgage Calculator")
# salary = int(input("What is your salary: "))
# if salary > 2000:
#     print("You are eligible for a mortgage.")
#     creditscore = int(input("What is your credit score: "))
#     if creditscore >= 900 and creditscore <= 1000:
#         rate = 3
#         print("Interest Rate is 3%")
#     elif creditscore > 800:
#         rate = 4
#         print("Interest Rate is 4%")
#     elif creditscore > 875000:
#         rate = 6
#         print("Interest Rate is 6%")    
#     else:
#         rate = 8
#         print("Interest Rate is 8%")
    
#     disability = input("Do you have any disability? Y or N: ")
    
#     if disability.upper() == "Y":
#         rate -= 2
#         print("You are eligible for a 2% discount due to disability.")
    
#     print(f"Final Interest Rate: {rate}%")
# else:
#     print("Sorry, you are not eligible.")        



# with try and except      
# print("Welcome to the Mortgage Calculator")
# try:
#     salary = int(input("What is your salary: "))
# except:
#     print("There was an error ")
# else:
#     if salary > 2000:
#         print("You are eligible ")
#     else:
#         print("You are not eligible ")
# finally:
#     print("Thanks for using our calculator")                    



# # print("Welcome to the Mortgage Calculator")
# try:
#     salary = int(input("What is your salary: "))
# except:
#     print("Enter an integer number. ") 
#     salary = int(input("What is your salary: "))
# else:
#     rate = 0 
#     if salary > 2000:
#         print("You are eligible for a mortgage.")
#         creditscore = int(input("What is your credit score: "))
#         if creditscore > 800:
#             rate = 4
#             print("Interest Rate is 4%")
#         elif creditscore > 750:
#             rate = 6
#             print("Interest Rate is 6%")
#         else:
#             rate = 8
#             print("Interest Rate is 8%")
#             disability = input("Do you have any disability? Y or N: ")
#             if disability.upper() == "Y":
#                 rate -= 2
#                 print("You are eligible for a 2% discount due to disability.")
            
#             print(f"Final Interest Rate: {rate}%")
#     else:
#             print("Sorry, you are not eligible.")
            
# finally:
#     print("Thanks for using our calculator ")            

      
    
# Project 6 Gross pay with overtime
# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")
# hour = float(hours)
# rate = float(rate)
# if hours < 40:
#     pay=round(hour*rate,2)
# else:
#     overtime = hour - 40
#     pay = round(40 * rate + overtime * rate *1.5,2)    
#     print(f"Pay: {pay}")




# Project 7 Leap Year
# year = int(input("Enter Year: "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap Year. ")
#         else:
#             print("Not Leap Year. ")    
#     else:
#         print("Leap Year. ")   
# else:
#     print("Not Leap Year. ") 



# Project 7 Love Calculator   
# print("Welcome to Love Calculator ")
# name1 = input("Enter your name: ")
# name2 = input("Enter your lover name: ")
# combibedname = name1 + name2
# lowercasename = combibedname.lower()
# t = lowercasename.count("t")
# r = lowercasename.count("r")
# u = lowercasename.count("u")
# e = lowercasename.count("e")
# true = t + r + u + e
# l = lowercasename.count("l")
# o = lowercasename.count("o")
# v = lowercasename.count("v")
# e = lowercasename.count("e")
# love = l + o + v + e
# lovescore =  int(str(true) + str(love))
# print(lovescore)

# if lovescore <10 or lovescore>85:
#     print(f"Your score is {lovescore}, you go together like coke and mentos. ")
# elif lovescore >= 40 and lovescore <= 70:
#     print(f"Your score is {lovescore}, you are alright together ")    
# else:
#     print(f"Your score is {lovescore}. ")    


# Project 9 Gross pay with Try and Exception
# hours = input("Enter Hours: ")
# try:
#     hour = float(hours)
# except ValueError:
#     print("Error, please enter numeric input for hour ")    
#     quit()
#     rate = input("Enter Rate: ")
# try:    
#     rate = float(rate)
# except ValueError:
#      print("Error, please enter numeric input for rate ")   
#      if hours < 40:
#             pay=round(hour*rate,2)
#      else:
#         overtime = hour - 40
#         pay = round(40 * rate + overtime * rate *1.5,2)    
#         print(f"Pay: {pay}")



# Project 10 Score Checker
# try:
#     score = float(input("Enter your Score: "))
# except ValueError:
#     print("Bad Score")
#     quit()    
# if score  >= 0.0 and score <=1.0:
#     if score >= 0.9:
#         print("A")
#     elif score >= 0.8:
#         print("B")
#     elif score >= 0.7:
#         print("C")
#     elif score >= 0.6:
#         print("D")
#     else:
#         print("F")                
# else:
#     print("Bad Score. ")  


# Functions in python
# import math
# result = math.sqrt(5)
# print(result)


# Area of a circle
# import math
# radius = int(input("Enter Radius:"))
# area = round(radius ** 2 * math.pi, 2)
# print(f"The area of circle is: {area}")


# Factorial
# import math
# num = int(input("Enter a number:"))
# factorial = math.factorial(num)
# print(f"The factorial of {num} is: {factorial}")

# Random number in python
# import random
# randomintegers =  random.randint(10,20)
# print(randomintegers)


# print("Welcome to Love Calculator ")
# name1 = input("Enter your name: ")
# name2 = input("Enter your lover name: ")
# combibedname = name1 + name2
# lowercasename = combibedname.lower()
# t = lowercasename.count("t")
# r = lowercasename.count("r")
# u = lowercasename.count("u")
# e = lowercasename.count("e")
# true = t + r + u + e
# l = lowercasename.count("l")
# o = lowercasename.count("o")
# v = lowercasename.count("v")
# e = lowercasename.count("e")
# love = l + o + v + e
# lovescore =  int(str(true) + str(love))
# print(lovescore)

# lovescore = random.randint(1,100)
# if lovescore <10 or lovescore>85:
#     print(f"Your score is {lovescore}, you go together like coke and mentos. ")
# elif lovescore >= 40 and lovescore <= 70:
#     print(f"Your score is {lovescore}, you are alright together ")    
# else:
#     print(f"Your score is {lovescore}. ")    


# Coin Toss
# import random
# result = random.randint(0,1)
# if result == 0:
#     print("Tails")
# else:
#     print("Heads")  



# User Defined Functions
# def firstfunction():
#     print("Hello, Iam a Function")
#     print("Bye for now")
# firstfunction()
# firstfunction()      


# def greet():
#     print("Hello")
#     print("How are you")
# greet()


# def greetwithname(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}")    
# greetwithname("Elshad")



# Area of square
# def area_of_square(side):
#     area = side * side
#     print(area)
# area_of_square(6)  


# Volume Converter
# def volume_converter(f_ounce):
#     m_liters = f_ounce * 29.57353
#     print(m_liters)
# volume_converter(5)   


# def greetwithNC(name, city):
#     print(f"Hello {name}")
#     print(f"What is weather like in {city}")
# greetwithNC("Elsha", "Berlin")    


# Painting Wall
# import math
# def calculate_can_number(height, width, coverage):
#     area = height * width
#     number_of_cans = math.ceil(area / coverage)
#     print(number_of_cans)
# height = int(input("Enter height of wall: "))
# width = int(input("Enter width of wall: "))
# calculate_can_number(height,width,4) 

# Functions with output
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title() 
#     return f"{formated_f_name}, {formated_l_name}" 
# output = format_name("elsahd", "karimov")                
# print(output)


# Exercise = Concatenate
# def concatenate(p1, p2):
#     con = p1 + p2
#     return con
# result = concatenate("face", "book")
# print(result)



# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "Name or LastName cannot be empty"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title() 
#     return f"{formated_f_name}, {formated_l_name}" 
# firstname = input("Enter Name: ")
# lastname = input("Enter LName: ")
# output = format_name(firstname, lastname)                
# print(output)



# Password Controller
# def password_controller(password):
#     if len(password) > 8:
#         return True
#     else:
#         return False
# result = password_controller("cust")    
# print(result)


# Docstrings
"""Hello we are learning python """


# Calculator
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# n1 = int(input("What is the first number? "))
# n2 = int(input("What is the second number? "))
# operation = input("Pick operation from this list (+,-,*,/) ")
# def calculate(n1, n2, operation):
#     if operation == "+":
#         return add(n1, n2)
#     elif operation == "-":
#         return subtract(n1, n2)
#     elif operation == "*":
#         return multiply(n1, n2)
#     elif operation == "/":
#         return divide(n1, n2)
#     else:
#         return "Invalid operation"
# output = calculate(n1, n2, operation)
# print(f"{n1} {operation} {n2} = {output}")
# newoperation = input("Pick another operation from this list (+,-,*,/) ")
# n3 = int(input("What is the third number? "))
# newoutput = calculate(output, n3, newoperation)
# print(f"{output} {newoperation} {n3} = {newoutput}")



# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(10, 20)
# print(result)



# def my_function(a):
#     if a < 20:
#         return
#         print("Bad")
#     if a < 80:
#         return "Passed"
#     else:
#         return "Good"
# print(my_function(15))


# Project 11 Leap Year with Function
# year = int(input("Enter Year: "))
# def leapyear(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return "Leap Year. "
#             else:
#                 return"Not Leap Year. "    
#         else:
#             return"Leap Year. "   
#     else:
#         return"Not Leap Year. " 
    
# result = leapyear(year)
# print(result)  


# Project 12 Gross Pay with functions
# def computepay(hour, rate):
#     if hours < 40:
#         pay=round(hour*rate,2)
#     else:
#         overtime = hour - 40
#         pay = (40 * rate) + (overtime * rate * 1.5)    
#     return pay    

# def checkforfloat(p_input):
#     try:
#         val = float(p_input)
#         return val
#     except ValueError:
#         print("Erro, please enter numeric input. ")
#         quit()
    
# hours = input("Enter Hours: ")
# hours = checkforfloat(hours)
# rate = input("Enter Rate: ")
# rate = checkforfloat(rate)  
# output = computepay(hours, rate)
# print(f"Pay: {output}")   
    
    
# Project 13 Cold, Warm and Hot
# def temperature(temp):
#     if temp > 28:
#         return "Hot"
#     elif temp > 18 and temp < 28:
#         return "Warm"
#     else:
#         return "Cold"
# temp = int(input("Enter temperature: "))
# result = temperature(temp)
# print(result)  




# Project 14 Maximum of three numbers
# def max(a,b,c):
#   if a>b and a>c:
#       return "A"
#   elif b>a and b>c:
#       return "B"
#   else:
#       return "C"      
# result = max(3,9,6)
# print(result)  

# def max_of_two(a, b):
#     if a > b:
#         return a
#     return b

# def max_of_three(a, b, c):
#     max_two = max_of_two(a, b)
#     max_three = max_of_two(max_two, c)
#     return max_three

# print(max_of_three(1, 2, 3))


# Python Lists
countrys = ["England", "Scotland"]

    