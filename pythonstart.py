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
# countrys = ["England", "Scotland", "Wales", "Nothern Ireland"]
# print(countrys[-1])
# countrys.append("Netherland")
# print(countrys)

# Loops
# vegetables = ["Carrot", "Brocolli", "Corn"]
# for vegetable in vegetables:
#     print(vegetable)
#     # print(vegetable + "pie")
# print(vegetables)


# Updating Variable
# a = 2
# a += 2
# print(a)
# nums = [1,2,3]
# s=0
# for num in nums:
#     s = s + num
#     print(s)


# Highest Score
# student_scores = [80, 60, 50, 65, 75, 55]
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The Highest score in the class is: {highest_score}")
    
    
# Find integers numbers
# custom_list = [11, 30.1, 90.2, 30, 45.1, 54, "54"]
# for item in custom_list:
#     if isinstance(item, int):
#         print(item)    


# Sum of above average scores
# student_scores = [80, 60, 50, 65, 75, 55]
# def sum_score_above_average(p_student_scores):
#     sum_score = 0
#     number_of_students = 0
#     for score in student_scores:
#         sum_score += score
#         number_of_students += 1
#     average_score =  sum_score / number_of_students
#     sum_above_average = 0
#     for score in p_student_scores:
#         if score > average_score:
#             sum_above_average += score
#     return sum_above_average
# print(sum_score_above_average(student_scores)) 




# Loop over custom function
# def password_controller(password):
#     if len(password) > 8:
#         return True
#     else:
#         return False
# # result = password_controller("cust")    
# # print(result)
# passwor_list = ["qwer", "123456", "098765432", "abcdefgh"]
# for password in passwor_list:
#     result = password_controller(password)
#     print(password, result)            
         
         

# For loop with range
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)



# Adding odd numbers
# def add_odd_numbers():
#     total = 0
#     for number in range(1, 101, 2):
#         total += number
#     return total    
# print(add_odd_numbers())
             
             
             
# Adding even numbers
# def add_even_numbers(start, end):
#     total = 0
#     for number in range(start, end+1):
#         if number % 2 == 0:
#             total += number
#     return total          
# print(add_even_numbers(1,100))


# While Loop
# Check Username
# username = ""
# while username != "test":
#     username = input("Enter Username: ")


# Iterations with continue and break
# for num in range(1,11):
#     if num == 5:
#         continue
#     print(num)
                

# num = 11
# while num > 0:
#     num -= 1
#     if num == 5:
#         continue
#     print(num)  


# num = 11
# while num > 0:
#     num -= 1
#     if num == 5:
#         break
#     print(num)   


# for num in range(1,11):
#     if num == 5:
#         break
#     print(num) 
# print("The End ")  



# Number Divisible by 5 until 130
# list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
# def numbers_divisible_byfive(p_list):
#     for item in p_list:
#         if item > 130:
#             break
#         if item % 5 == 0:
#             print(item)
#     print("STOP") 
# numbers_divisible_byfive(list1)          
                             
             
# Factorial using loop
# def factorial(p_num):
#     factorial = 1
#     if p_num < 0:
#         return "Factorial does not exist for negative numbers"
#     if p_num == 0:
#         return "The factorial of 0 is 1"
#     else:
#         for num in range(1, p_num + 1):
#             factorial = factorial * num
#         return f"The factorial of {p_num} is {factorial} "
# print(factorial(4))  



# Sum, Count and Average of Entered Numbers
# def check_for_float(p_input):
#     try:
#         val = float(p_input)
#         return val
#     except (ValueError, TypeError):
#         print("Error, please enter numeric input")
#         return False
    
# count = 0
# total = 0.0
# average = 0.0
# while True:
#     input_number = input("Enter a number: ")
#     if input_number == "done":
#         break
#     number = check_for_float(input_number)
#     if not number:
#         continue
#     count+=1
#     total = total + input_number
# if count != 0:    
#   average = total / count        
# print(total, count, average)    


# Maximum and Minimum of Input Numbers      
# def check_for_float(p_input):
#     try:
#         val = float(p_input)
#         return val
#     except (ValueError, TypeError):
#         print("Error, please enter numeric input")
#         return False 
# input1 = input("Enter a number: ")
# if input1 == "done":
#     quit()
# number = check_for_float(input1) 
# if not number:
#     print("The first entered has to be number to comtinue")    
# smallest = number
# biggest = number
# while True:
#     input1 = input("Enter a number: ")
#     if input1 == "done":
#         break
#     number = check_for_float(input1)
#     if number > biggest:
#         biggest = number
#     if number < smallest:
#         smallest = number
# print(f"Maximum number: {biggest}, Minimum number: {smallest}")        
                                              

# Project 15 Dice Rolling Simulator
# import random
# rollagain = "Y"
# while rollagain == "Y":
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     print(f"Dice1: {dice1}", f"\nDice2: {dice2}")
#     rollagain = input("Roll the dice again? (Y?N)")



# Project 16 Fizz Buzz Game
# for num in range(1, 101):
#     if num % 5 == 0 and num % 7 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 7 == 0:
#         print("FizzBuzz") 
#     else:
#         print(num)  



# Project 17 Guessing the number 
# import math
# import random
# lower = input("Enter Lower bound: ")
# upper = input("Enter upper bound: ") 
# numberofchances = int(math.log(upper-lower+1,2))  
# print(f"\n\tYou've only {numberofchances} chances to guess the integer!\n ")
# generatednumber = random.randint(lower, upper) 
# count = 0
# while count < numberofchances:
#     count += 1
#     guess = int(input("Guess a number: "))
#     if generatednumber == guess:
#         print(f"Congratulations you did it in {count} try ")
#         break
#     elif guess > generatednumber:
#         print("You guessed too high ")
#     elif guess < generatednumber:
#         print("You guessed too low ")
# print(f"\nThe number is {generatednumber} ")
# print(f"\nBetter luck next time ")


# Project 18 password generator
# import random

# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "1234567890"
# symbols = "-+=!@#$%^&*"

# numberofletters = int(input("How many letters do you want in your password: "))
# numberofnumbers = int(input("How many numbers do you want in your password: "))
# numberofsymbols = int(input("How many symbols do you want in your password: "))

# # Generate characters
# password = ""
# for _ in range(numberofletters):
#     password += random.choice(letters)
# for _ in range(numberofnumbers):
#     password += random.choice(numbers)
# for _ in range(numberofsymbols):
#     password += random.choice(symbols)

# # Shuffle the password
# password_list = list(password)
# random.shuffle(password_list)
# final_password = ''.join(password_list)

# # Output
# print(f"\nYour Password is: {final_password}")


# Project 19 Rock, Paper, Scissors
# import random

# def select_computer_action():
#     possible_actions = ["rock", "paper", "scissors"]
#     return random.choice(possible_actions)

# def determine_winner(computer_action, user_action):
#     if user_action == computer_action:
#         print(f"Both selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    
#     # Ensure valid input
#     if user_action not in ["rock", "paper", "scissors"]:
#         print("Invalid choice. Try again.")
#         continue

#     computer_action = select_computer_action()
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.")
#     determine_winner(computer_action, user_action)

#     play_again = input("\nPlay again? (Y/N): ").upper()
#     if play_again != "Y":
#         print("Thanks for playing!")
#         break



# Strings in python
# myname = 'elsahd'
# fruit = "apple"
# print(len(fruit))
# a = 3
# letter = fruit[1]
# print(a)

# newstring = "Hello Python"
# print(newstring[0:7])
# print(newstring[:])


# Sum of Digits of 2 digit number
# def sum_of_two_digits():
#     two_digit_number = input("Enter two digit number: ")
#     sum_of_digits = int(two_digit_number[0]) + int(two_digit_number[1])
#     return sum_of_digits
# print(sum_of_two_digits())



# String Traversal
# fruit = "orange"
# for char in fruit:
#     print(char)

# index = 0
# while index < len(fruit):
#     letter = fruit(index)
#     print(letter)
#     index += 1


# coding exercise string backward traversal
# new_string = input("Enter a string: ")
# index = -1
# length = -1 * len(new_string)
# while index >= length:
#     letter = new_string[index]
#     print(letter)
#     index -= 1


# coding exercise sum of digits
# number  = input("Enter an integer number: ")
# sum_digits = 0
# for num in number:
#     sum_digits += int(num)
# print(sum_digits)



# coding exercise count characters in a string
# def count_letter(word, letter):
#     counter = 0
#     for char in word:
#         if char == letter:
#             counter += 1
#     return counter
# print(count_letter("Learning python", "n"))


# string operation
# str1 = "Hello"
# str2 =  "World"
# print(str1 + str2)

# newstring = input("Enter a string: ")
# if newstring < "hello":
#     print(F"your word {newstring} comes before hello")
# elif newstring > "hello":
#     print(f"your word {newstring} comes after hello")


# coding exercise first and last two characters
# def first_last_characters(word):
#     if len(word) < 2:
#         return ''
#     first_two_chars = word[0:2]
#     last_two_chars = word[-2:]
#     return first_two_chars + last_two_chars
# print(first_last_characters("appmillers"))  


# String methods
# myname = "Elhsad" 
# print(dir(myname)) 


# coding exercise replace character in a string
# custom_string = 'I love Python.I Like Learning it.'
# new_string = custom_string.replace(".", "!", 2)
# print(custom_string)
# print(new_string)


# String parsing
# data = 'from example.email@edu.co.uk sat sep 5 09:14:16 2021'
# at_index = data.find("@")
# print(at_index)
# sapce_after = data.find(' ', at_index)
# print(sapce_after)
# domain = data[at_index+1:sapce_after]
# print(domain)


# mystring = "I love learning python"
# output = mystring.split("_", maxsplit=2)
# print(output)
# joinback = "_".join(output)
# print(joinback)


# triple quotes
# question = '''He said "What's your name?" '''
# print(question)

# escaping single quotes
# question = 'He said "What\s your name" '''
# print(question)

# escaping double quotes
# question = "He said \"What's your name?\""
# print(question)


# path = "C:\Python\nib"
# print(path)


# String Formatting
# errorno = 45457984738
# name = 'Edy'
# print('Hello, %s' %name)
# print('%x' %errorno)
# print('Hey %s, there is a 0x%x error' %(name, errorno))

# print('Hello, {}'.format(name))
# print('Hey{}, there is a 0x{} error!'.format(name, errorno))



# coding exercise format a string
# custom_string = "X-MAPDS-Confidence:0.8475"
# index_col = custom_string.find(":")
# number = custom_string[index_col + 1 : ]
# number = float(number)
# print(number)


# coding exercise print pattern
# def print_pattern(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print("*", end = ' ')
#         print()   
#     for i in range(n, 0, -1):
#         for j in range(0, i-1):
#             print("*", end=' ')
#         print()
# print_pattern(4)             



# project 20 String Formatting
# names = ['John', 'Edy', 'Jane', 'Kane']
# scores = [90, 95, 80, 75]
# print('{0:<10} {1:<5}'.format("Name", "Score"))
# for index in range(len(names)):
#     name = names[index]
#     score = scores[index]
#     print('{0:<10} {1:<5}'.format(name, score))



# coding exercise square of items
# def square_list(p_list):
#     for index in range(len(p_list)):
#         p_list[index] = p_list[index] * p_list[index]
#     return p_list

# custom_list = [1,2,3,4,5,6,7,8,9,10]
# print(square_list(custom_list))    



# index out of range
# countriesofuk = ["England", "Scotland", "Nothern Ireland", "Wales"]
# numofcountries = len(countriesofuk)
# print(numofcountries)



# Slicing
# mylist = ['a', 'b', 'c', 'd', 'd']
# mylist[1:3] = ['x', 'y']
# print(mylist)



# + Operator (Concatenate)
# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = list1 + list2
# print(list3)


# * Operator
# list1 = [1]
# list2 = list1 * 4
# print(list2)


# in keyword
# list1 = [1,2,4, 'a', 'b', 'c', 'd']
# print('a' in list1)
# print(5 in list1)



# coding exercise reverse a list using slice operator
# custom_list = [1,2,3,4,5,6,7,8,9,10]
# custom_list = custom_list[::-1]
# print(custom_list)


# List Method practice
# animals = ['dog', 'cat', 'mouse', 'horse', 'bear']
# animals2 = ['fox', 'rabbit']
# index = animals.index('horse')
# print(index,4,5)
# animals.extend(animals2)
# animals.append('fox')
# animals.insert(2, 'rabbit')
# animals.remove('bear')
# count = animals.count('horse')
# animals.pop(1)
# animals.reverse()
# animals.sort()
# animals.sort(reverse=True)
# newanimals = animals.copy()
# print(animals)
# animals.clear()
# print(animals)




# coding exercise update the first occurrence
# list1 = [10,10,5,15,50,50,20]
# index = list1.index(50)
# list1[index] = 5
# print(list1)



# coding exercise first and last characters
# list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
# def count_words(p_list):
#     ctr = 0
#     for word in p_list:
#         if len(word) >= 2 and word[0] == word[-1]:
#             ctr +=1
#     return ctr
# print(count_words(list1)) 



# List and functions
# nums = [10,15,20,30,5]
# del nums[1]
# print(nums)


# numlist = []
# while True:
#     inp = input("Enter a number: ")
#     if inp == "done":
#         break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist) 
# print(f"Average: {average}")          




# coding exercise create a list from two lists
# list_one = [4,12,16,21,24,28,32]
# list_two = [5,10,15,20,25,30,35]
# third_list = list()
# odd_elements = list_one[1::2]
# print(odd_elements)
# even_elements = list_two[0::2]
# print(even_elements)
# third_list.extend(odd_elements)
# third_list.extend(even_elements)
# print(third_list)


# coding exercise remove and add value
# custom_list = [10,44,57,99,11,33,84]
# element = custom_list.pop(4)
# custom_list.insert(2, element)
# custom_list.append(element)
# print(custom_list)



# coding exercise Three equal chunks
# sample_list = [21,55,18,33,24,22,68,35,79]
# length = len(sample_list)
# chunk_size = int(length/3)
# start = 0
# end = chunk_size
# for i in range(1,4):
#     list_chunk = sample_list[start:end]
#     reversed_chunk = reversed(list_chunk)
#     print(f"Chunk-{i} = {list(reversed(list_chunk))}")
#     start = end
#     end += chunk_size



# String and list
# custom_string = "hello world. I love python"
# # custom_list = list(custom_string)
# custom_list = ['Jane', 'Edy', 'John']
# string1 = "_".join(custom_list)
# # custom_list = custom_string.split()
# print(custom_list)



# coding exercise Format List
# custmo_list = [1,2,3,4,5]
# output_list = []
# for item in custmo_list:
#     output_list.append(str(item))
# custom_string = " | ".join(output_list)
# print(custom_string)


# Nested List
# day1 = [11,12,5,2]
# day2 = [15,11,6,7]
# day3 = [10,13,7,5]
# day4 = [12,15,8,6]
# alldays = [day1, day2, day3, day4]
# print(alldays)


# mylist = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
# mylist[2].append('ggg')
# mylist[2][2].insert(0, "ggg")
# mylist[2].extend([1,2,3])
# mylist[2][2].pop(0)
# del mylist[2][2][0]
# length = len(mylist[2])
# print(mylist)
# mylist[1] = 0
# print(mylist)
# for item in mylist:
#     for item2 in item:
#         for item3 in item2:
#             print(item2)


# coding exercise Add item in Nested List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].insert(1, 7000)
# print(list1)



# coding exercise Extend Nested List
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sublist = ['h', 'i', 'j']
# list1[2][1][2].extend(sublist)
# print(list1)



# Objects and Values
# True
# a = "apple"
# b = "apple"
# False
# a = [1,2,3]
# b = [1,2,3]
# print(a is b)

# def deletefirst(p_list):
#     del p_list[0]
# mylist = [1,2,3,4,5]
# deletefirst(mylist)
# print(mylist)    


# coding exercise List Addition with function
# def custom_insert(p_list, value):
#     copy_list = p_list[:]
#     copy_list.append(value)
#     return copy_list
# list1 = [1,2,3,4,5]
# list2 = custom_insert(list1, 6)
# print(list1)
# print(list2)


# coding exercise Concatenate two list in one list item wise
# def concatenate(p_list1, p_list2):
#     list3 = []
#     for item1 in p_list1:
#         for item2 in p_list2:
#             list3.append(item1 + item2)
#     return list3
# list1= ["Hello ", "take "]
# list2= ["Dear ", "Sir "]
# concatenate(list1, list2)   


# Project 21 Bill Roulette
# import random
# name_string = input("Input everyone's name, seperated by a comma. ")
# names = name_string.split(", ")
# num_items = len(names)
# random_list = random.randint(0, num_items-1)
# person_names = names[random_list]
# print(f"{person_names} is going to buy the meal today! ")         




# Project 22 Find the Golden Star
# import random
# def print_map(p_map):
#     print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

# map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
# print("This is our initial map...")
# print_map(map1)
# gold_hor = random.randint(0,2)
# gold_ver = random.randint(0,2)
# map1[gold_hor][gold_ver] = "⭐️"
# goldposition = str(gold_hor+1) +str(gold_ver+1)
# position = input("What do you think: where is the Golden Star in the map? ")
# if goldposition == position:
#     print("Congratulations! You have found the Golden Star")
# else:
#     horizontal = int(position[0])
#     vertical = int(position[1])
#     map1[horizontal-1][vertical-1] = "*"
#     print("Unfortunately you could find it. ") 
# print_map(map1)




# import random
# def print_map(p_map):
#     print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

# map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
# print("This is our initial map...")
# print_map(map1)

# gold_horizontal = random.randint(0,2)
# gold_vertical = random.randint(0,2)
# map1[gold_horizontal][gold_vertical] = "⭐️"
# gold_position = str(gold_horizontal+1) + str(gold_vertical+1)

# position = input("What do you think: where is the Golden Star in the map? ")

# if gold_position == position:
#     print("Congratulations!!! You have found the Golden STAR!")
# else:
#     horizontal = int(position[0])
#     vertical = int(position[1])
#     map1[horizontal-1][vertical-1] = "🆇"
#     print("Unfortunatly you could find it 🙁")

# print_map(map1)


    
    
    
# Project 22 Escaping the Maze (with reeborgs wordl)
# def turnright():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move() 
# turn_left()       
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()   
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()



# Project 24 Cryptography with python Caesar Cipher
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# message = input("Enter your message:\n").upper()
# shift_number = int(input("Enter the shift number:\n"))
# # Encryption
# def encrypt(p_message, p_shift_number):
#     cipher_message = " "
#     for char in p_message:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + p_shift_number
#             while new_position > 25:
#                 new_position = new_position - 26
#             new_char = alphabet[new_position]
#             cipher_message += new_char
#         else:
#             cipher_message += char   
#     return f"The encoded message is {cipher_message}"
# encoded_message = encrypt(message, shift_number)
# print(encoded_message)



# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
# cipher_message = input("Enter your message:\n").upper()
# shift_number = int(input("Enter the shift number:\n"))
# def decrypt(p_message, p_shift_number):
#     message = ""
#     for char in p_message:
#         if char in alphabet:
#             position = alphabet.index(char)
#             old_position = position - p_shift_number
#             while old_position < 0:
#                 old_position = old_position + 26
#             letter = alphabet[old_position]
#             message += letter
#         else:
#             message += letter    
#     return f"The decoded text is {message}"
# print(decrypt(cipher_message, shift_number))        
         
    



# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']




# def encrypt(p_message, p_shift_number):
#     cipher_message = " "
#     for char in p_message:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + p_shift_number
#             while new_position > 25:
#                 new_position = new_position - 26
#             new_char = alphabet[new_position]
#             cipher_message += new_char
#         else:
#             cipher_message += char   
#     return f"The encoded message is {cipher_message}"
# encoded_message = encrypt(message, shift_number)
# print(encoded_message)



# def decrypt(p_message, p_shift_number):
#     message = ""
#     for char in p_message:
#         if char in alphabet:
#             position = alphabet.index(char)
#             old_position = position - p_shift_number
#             while old_position < 0:
#                 old_position = old_position + 26
#             letter = alphabet[old_position]
#             message += letter
#         else:
#             message += letter    
#     return f"The decoded text is {message}"
# print(decrypt(cipher_message, shift_number)) 



# from logo import logo
# print(logo)
# end_program = False
# while not end_program:
#     enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
#     message = input("Enter your message:\n").upper()
#     shift_number = int(input("Enter the shift number:\n"))
#     if enc_dec == "E":
#         encrypted_message = encrypt(message, shift_number)
#         print(encrypted_message)
#     else:
#         decrypt_message = decrypt(cipher_message, shift_number)
#         print(decrypt_message) 
#     restart = input("Type 'Y' if you want to continue. otherwise type 'N'\n")
#     if restart == "N":
#         end_program = True
#         print("See you next time")            







# Caesar Cipher Program

# Alphabet list
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# # Encryption function
# def encrypt(p_message, p_shift_number):
#     cipher_message = ""
#     for char in p_message:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = (position + p_shift_number) % 26
#             cipher_message += alphabet[new_position]
#         else:
#             cipher_message += char   
#     return f"The encoded message is: {cipher_message}"

# # Decryption function
# def decrypt(p_message, p_shift_number):
#     message = ""
#     for char in p_message:
#         if char in alphabet:
#             position = alphabet.index(char)
#             old_position = (position - p_shift_number) % 26
#             message += alphabet[old_position]
#         else:
#             message += char    
#     return f"The decoded message is: {message}"

# # Main loop
# end_program = False
# while not end_program:
#     enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n").upper()
#     message = input("Enter your message:\n").upper()
#     shift_number = int(input("Enter the shift number:\n"))

#     if enc_dec == "E":
#         encrypted_message = encrypt(message, shift_number)
#         print(encrypted_message)
#     elif enc_dec == "D":
#         decrypted_message = decrypt(message, shift_number)
#         print(decrypted_message)
#     else:
#         print("Invalid option. Please type 'E' or 'D'.")

#     restart = input("Type 'Y' if you want to continue, otherwise type 'N':\n").upper()
#     if restart == "N":
#         end_program = True
#         print("See you next time!")




# Caesar Cipher Program

# Alphabet list
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# # Recalculate position for encryption or decryption
# def refactor_position(p_position, p_cipher_type):
#     if p_cipher_type == 'E':
#         while p_position > 25:
#             p_position -= 26
#         return p_position
#     else:
#         while p_position < 0:
#             p_position += 26
#         return p_position

# # Core Caesar cipher function
# def caesar_cipher(p_initial_text, p_shift_amount, p_cipher_type):
#     final_text = ""
#     if p_cipher_type == "D":
#         p_shift_amount *= -1

#     for char in p_initial_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + p_shift_amount
#             new_position = refactor_position(new_position, p_cipher_type)
#             final_text += alphabet[new_position]
#         else:
#             final_text += char

#     action = "decoded" if p_cipher_type == "D" else "encoded"
#     print(f"Here's the {action} result: {final_text}")



# Main program loop
# end_program = False
# while not end_program:
#     enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n").upper()
#     text = input("Enter your message:\n").upper()
#     shift = int(input("Enter the shift number:\n"))

#     caesar_cipher(p_initial_text=text, p_shift_amount=shift, p_cipher_type=enc_dec)

#     restart = input("Type 'Y' if you want to go again. Otherwise type 'N':\n").upper()
#     if restart == "N":
#         end_program = True
#         print("See you next time!")




# Project 25 Story Generator
# def sentence_maker(text):
#     words = ['what', 'how', 'where']
#     cap_text = text.capitalize()
#     for word in words:
#         if text.startswith(word):
#             return "{}?".format(cap_text)
#     return "{}.".format(cap_text)
  

# result = []
# while True:
#     user_input = input("What is on your mind. ")
#     if user_input == "\end":
#         break
#     else:
#         complete_sentence = sentence_maker(user_input)
#         result.append(complete_sentence)
# story = " ".join(result)
# print(story)


# Hangman, Flowchart, Pick Secret Word, Check letters and track lives
# hangman_stages = ['''
#   +---+
#   |   |
#   |   O
#   |  /|\  
#   |  / \ 
#   |    
# ==========
# ''', '''
#   +---+
#   |   |
#   |   O
#   |  /|\  
#   |  / 
#   |    
# ==========
# ''', '''
#   +---+
#   |   |
#   |   O
#   |  /|\  
#   |  
#   |    
# ==========
# ''', '''
#   +---+
#   |   |
#   |   O
#   |  /| 
#   |  
#   |    
# ==========''', '''
#   +---+
#   |   |
#   |   O
#   |   |
#   |  
#   |    
# ==========
# ''', '''
#   +---+
#   |   |
#   |   O
#   |   
#   |  
#   |    
# ==========
# ''', '''
#   +---+
#   |   |
#   |   
#   |   
#   |  
#   |    
# ==========
# ''']

# word_list = ["UDEMY", "APPMILLERS", "PYTHON"]
# import random
# secret_word = random.choice(word_list)
# length_word = len(secret_word)
# print(secret_word)
# blanks = []

# for _ in range(length_word):
#     blanks.append("_")

# guessed_letters = []
# lives = 6
# end_game = False
# while not end_game:
#     guess = input("Guess a letter: ").upper()
#     if guess in guessed_letters:
#         print("You have already guessed this letter!")
#         continue
#     else:
#         guessed_letters.append(guess)

#     for position in range(length_word):
#         letter = secret_word[position]
#         if guess == letter:
#             blanks[position] = letter
    
#     if guess not in secret_word:
#         lives -= 1
#     if lives == 0:
#         end_game = True
#         print("You lose!")
#     print(" ".join(blanks))
#     print(hangman_stages[lives])
#     if "_" not in blanks:
#         end_game = True
#         print("You win.")
#     if end_game:
#         ask = input("Do you want to play again? (Y/N)")
#         if ask == "Y":
#             secret_word = random.choice(word_list)
#             blanks.clear()
#             length_word = len(secret_word)
#             for _ in range(length_word):
#                 blanks.append("_")
#             end_game = False
#             guessed_letters.clear()
#             lives = 6
#         else:
#             print("See you next time!")





# import random
# import os

# # function to clear terminal screen
# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Hangman logo (optional ASCII art)
# logo = """
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/                       
# """

# # Hangman stages (ASCII art)
# hangman_stages = [
#     """
#        --------
#        |      |
#        |      O
#        |     \\|/
#        |      |
#        |     / \\
#        -
#     """,
#     """
#        --------
#        |      |
#        |      O
#        |     \\|/
#        |      |
#        |     / 
#        -
#     """,
#     """
#        --------
#        |      |
#        |      O
#        |     \\|/
#        |      |
#        |      
#        -
#     """,
#     """
#        --------
#        |      |
#        |      O
#        |     \\|
#        |      |
#        |     
#        -
#     """,
#     """
#        --------
#        |      |
#        |      O
#        |      |
#        |      |
#        |     
#        -
#     """,
#     """
#        --------
#        |      |
#        |      O
#        |    
#        |      
#        |     
#        -
#     """,
#     """
#        --------
#        |      |
#        |      
#        |    
#        |      
#        |     
#        -
#     """,
# ]

# print(logo)

# word_list = ["APPMILLERS", "UDEMY"]
# secret_word = random.choice(word_list)
# word_length = len(secret_word)
# guessed_letters = []
# blanks = ["_"] * word_length
# lives = 6

# end_game = False
# while not end_game:
#     guess = input("Guess a letter: ").upper()
#     clear()

#     if guess in guessed_letters:
#         print("You have already guessed this letter!")
#         continue
#     else:
#         guessed_letters.append(guess)

#     for position in range(word_length):
#         letter = secret_word[position]
#         if guess == letter:
#             blanks[position] = letter

#     if guess not in secret_word:
#         lives -= 1
#         if lives == 0:
#             end_game = True
#             print("You Lose.")
#             print(f"The word was: {secret_word}")

#     print(" ".join(blanks))
#     print(hangman_stages[lives])

#     if "_" not in blanks:
#         end_game = True
#         print("You win!")

#     if end_game:
#         ask = input("Do you want to play again?(Y/N) ").upper()
#         if ask == "Y":
#             secret_word = random.choice(word_list)
#             blanks = ["_"] * len(secret_word)
#             guessed_letters.clear()
#             lives = 6
#             end_game = False
#         else:
#             print("See you next time!")



# Dictionaries in Python
# mydictionary = {"Miller" : "a person who owns or works in a corn mill",
#                 "Programmer" : "a person who writes a computer program",
#                 "App" : "an application, especially as downloaded by a user to a mobile device ",
#                 123 : "One Two Three"}
# print(mydictionary)
# mydictionary = dict()
# print(mydictionary)

# mylist = ["Miller", "Programmer", "App"]
# print(mylist[1])

# mydictionary = {}
# print(mydictionary)
# mydictionary['Miller'] = 'a person who owns or works in a corn mill'
# mydictionary['Programmer'] = 'a person who writes a computer program'
# print(mydictionary)
# print(mydictionary['Programmer'])




# Coding exercise Generate Dictionary
# def genrate_dictionary(n):
#     my_dict = dict()
#     for num in range(1, n+1):
#         my_dict[num] = num * num
#     return my_dict
# output = genrate_dictionary(5)
# print(output)




# mydictionary = {"Miller" : "a person who owns or works in a corn mill",
#                 "Programmer" : "a person who writes a computer program",
#                 "App" : "an application, especially as downloaded by a user to a mobile device ",
#                 123 : "One Two Three"}

# for key in mydictionary:
#     if key == "App":
#         print("Key Exists")
#         print(mydictionary[key])



# Coding exercise Multiply dictionary items
# my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
# def multiply_values(p_dict):
#     output = 1
#     for key in p_dict:
#         output = output * p_dict[key]
#     return output
# print(multiply_values(my_dict))




# Coding exercise Student Grades
# student_scores = {
#     "John" : 90,
#     "Edy" : 68,
#     "Marry" : 88,
#     "Ewan" : 79,
#     "Park" : 62,
# }
# def convert_grade(p_dict):
#     student_grades = {}
#     for key in p_dict:
#        score = p_dict[key]
#        if score >= 85:
#            student_grades[key] = "Outstanding"
#        elif score >= 65:
#            student_grades[key] = "Good"
#        elif score >= 50:
#            student_grades[key] = "Acceptable"
#        else:
#            student_grades[key] = "Fail"
#     return student_grades
           
           
# print(convert_grade(student_scores))

        
      
    

# Remove items
# mydictionary = {"Miller" : "a person who owns or works in a corn mill",
#                 "Programmer" : "a person who writes a computer program",
#                 "App" : "an application, especially as downloaded by a user to a mobile device ",
#                 123 : "One Two Three"}

# result = mydictionary.pop("Programmer", None)
# print(result)
# print(mydictionary) 


# result = mydictionary.popitem()
# print(result)
# print(mydictionary)  


# del mydictionary['Miller']
# print(mydictionary)  




# Coding exercise rename to key
# my_dict = {
#     "name" : "Edy",
#     "age" : 30,
#     "salary" : 5000,
#     "city" : "London",
# }
# my_dict["address"] = my_dict.pop("city")
# print(my_dict)


# IN/NOT IN Operator
# list1 = [1,2,3,4,5,6]
# string1 = "I Love Python"
# # print("Like" not in string1)
# my_dict = {
#     1:"one",
#     2:"two",
#     3:"three"
# }
# print(9 not in my_dict)




# Coding exercise solution to count the characters in a word
# def count_character(word):
#     output_dict = dict()
#     for character in word:
#         print(character)
#         if character not in output_dict:
#             output_dict[character] = 1
#         else:
#             output_dict[character] = output_dict[character] + 1
#     return output_dict
# print(count_character("BABACDAS"))
         
         
         
# Nested Dictionaries
# programming_language = {
#     "Elshad" : { "Favorite_language" : ["Python", "Java", "C++"], "experience" : 10
#                 },
#     "Renad" : {"Favorite_language" : ["Scratch", "Python"],
#                "experience" : 2
#     },
#     "Edy" : "Java",
# }
# mylist = [1,2,3,4,5,[1,2],[4,5]]



# # Nested dictionary inside list
# programming_language =[ {
#     "username" : "Elshad",
#     "favorite_language" : ["python", "java", "c++"],
#     "experience" : 10
# },
# {
# "username" : "Renad",
#     "favorite_language" : ["scratch", "java"],
#     "experience" : 2
# },
# ]





# Coding exercis nested dictionaries
# programming_language = {
#     "Elshad" : { "Favorite_language" : ["Python", "Java", "C++"], "experience" : 10
#                 },
#     "Renad" : {"Favorite_language" : ["Scratch", "Python"],
#                "experience" : 2
#     },
#     "Edy" : "Java",
# }
# mylist = [1,2,3,4,5,[1,2],[4,5]]



# Nested dictionary inside list
# programming_language =[ {
#     "user_name" : "Elshad",
#     "favorite_languages" : ["Python", "Java", "C#"],
#     "experience" : 10
# },
# {
# "user_name" : "Renad",
#     "favorite_languages" : ["Scratch", "Python"],
#     "experience" : 2
# },
# ]
# def add_new_user(p_user_name, p_favorite_languages, p_experience):
#     new_user = {}
#     new_user["user_name"] = p_user_name
#     new_user["favorite_languages"] = p_favorite_languages
#     new_user["experience"] = p_experience
#     programming_language.append(new_user)
#     print(programming_language)
# add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)




# Handling missing keys in dictionary
# items = {
#     "computer" 
#     "printer" : 8,
#     "mouse" : 15,
#     "webcam" : 12,
#     "router" : 10,
# }
# quatity = items.get("microphone")
# print(f"Number of microphones in the store: {quatity}")
# quatity = items.setdefault("computer", 11)
# print(f"Number of microphones in the store: {quatity}")



# keys in dictionary
# custom_dict = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
# }
# devices_list = {"phone", "tablet", "computer", "tv"}
# new_dict = {}.fromkeys(devices_list, 0)
# print(new_dict)

# keys = custom_dict.keys()
# print(keys)


# Coding exercise solution to group value type
# custom_list = [10,"one", "two", "ten", 20,30,"five", 40,"nine", 50]
# def group_types(p_list):
#     output_dict = dict.fromkeys(p_list)
#     for key in output_dict:
#         if isinstance(key, int):
#             output_dict[key] = "Integer"
#         else:
#             output_dict[key] = "String"
#     return output_dict
# print(group_types(custom_list))



# Dictionary item() method
# custom_dict = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
# }
# for item in custom_dict:
#     print(item, custom_dict)
    
# print()

# for key, value in custom_dict.items():
#     print(key, value)



# coding exercise length of dictionary values
# names_dict = {
#     1 : "Elshad",
#     2 : "Renad",
#     3 : "Johanna",
#     4 : "Appmillers"
# }
# def value_length(p_dict):
#     output_dict = {}
#     for key, value in p_dict.items():
#         output_dict[key] = {}
#         output_dict[key][value] = len(value)
#     return output_dict
# print(value_length(names_dict)) 




# Dictionary update method
# custom_dict = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six"
# }

# custom_dict2 = {
#     8: "eight",
#     9: "nine",
#     1: "one",
#     2: "two"
# }
# custom_dict.update(custom_dict2)
# for key, value in custom_dict.items():
#     print(key, value)



# coding exercise concatenate three dictionaries
# dict1 = {1: "one", 2: "two"}
# dict2 = {3: "three", 4: "four"}
# dict3 = {5: "five", 6: "six"}
# def concatenate(d1, d2, d3):
#     new_dict = {}
#     for dic in [d1, d2, d3]:
#         new_dict.update(dic)
#     return new_dict
# print(concatenate(dict1, dict2, dict3))



# Dictionary value method
# custom_dict = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six"
# }
# values = custom_dict.values()
# print(values)

# custom_dict[8] = "eight"
# print(values)

# print("five" in values)
# print("ten" in values)

# values = list(custom_dict.values())
# keys = list(custom_dict.keys())
# if "five" in values:
#     index = values.index("five")
#     key = keys[index]
#     print(f"{custom_dict[key]} is found with the key {key}")
    
# for key, value in custom_dict.items():
#     if value == "five":
#         print(f"{custom_dict[key]} is found with the key {key}")



# coding exercise remove empty items
# custom_dict = {
#     "name": "Elshad",
#     "age": 28,
#     "city": None
# }
# def remove_empty_items(p_dict):
#     for key, value in list(p_dict.items()):
#         if value is None:
#             p_dict.pop(key)
#     return p_dict
# print(remove_empty_items(custom_dict))




# Reference to dictionary copy() method
# namelist = ["Edy", "John", "Ewan"]
# citylist = ["London", "Berlin", "Paris"]
# languagelist = ["English", "German", "French"]
# person = {
#     "name": namelist,
#     "city": citylist,
#     "Language": languagelist,
# }

# person2 = {
#     "name": namelist,
#     "city": citylist,
#     "Language": languagelist,
# }

# newperson = person.copy()
# # person["city"] = "Berlin"
# person["city"].append("Appended using person dict")
# newperson["city"].append("Appended using new person dict")
# citylist.append("Appended by itself")
# print(person["city"])
# print(newperson["city"])




# coding exercise merge two dictionary
# dict1 = {"One":2, "Two":2, "Three":3}
# dict2 = {"Three":3, "Four":4, "Five":5}
# def merge_dict(p_dict1, p_dict2):
#     dict3 = p_dict1.copy()
#     dict3.update(p_dict2)
#     return dict3
# print(merge_dict(dict1, dict2))
# print(dict1)
# print(dict2)
    
    
    
# Deep Copy
# import copy
# namelist = ["Edy", "John", "Ewan"]
# citylist = ["London", "Berlin", "Paris"]
# languagelist = ["English", "German", "French"]
# person = {
#     "name": namelist,
#     "city": citylist,
#     "Language": languagelist,
# }

# # newperson = person.copy()
# # deep copy
# newperson = copy.deepcopy(person)
# newperson["city"].append("Madrid")
# print(newperson["city"])
# print(person["city"])
# print(id(newperson["city"]), newperson["city"])




# coding exercise custom deep copy for list values
# original_dict = {
#     "names" : ["Edy", "John", "Ewan"],
#     "numbers" : [1,2,3,4,5]
# }
# def deep_copy(p_dict):
#     new_dict = {}
#     for key, value in p_dict.items():
#         new_value = value.copy()
#         new_dict[key] = new_value
#     return new_dict

# copied_dict = deep_copy(original_dict)
# copied_dict["names"].append("Jack")
# copied_dict["numbers"].append(6)
# print(original_dict)
# print(copied_dict)



# Dictionary operations
# mydict = {
#     3:"three",
#     5:"five",
#     9:"nine",
#     2:"two",
#     1:"one",
#     4:"four",
# }

# mydict1 = {
#     1:"zero",
#     False : "False"
# }
# print(len(mydict1))
# print(all(mydict1))
# print(any(mydict1))





# Project 27 Calculate total price
# available_parts = {
#     "1":"computer",
#     "2":"monitor",
#     "3":"keyboard",
#     "4":"mouse",
#     "5":"hdmi cable",
#     "6":"dvd drive",
# }
# price_quantity = {
#     "computer": {"price":500, "quantity": 10},
#     "monitor": {"price":200, "quantity": 8},
#     "keyboard": {"price":500, "quantity": 5},
#     "mouse": {"price":10, "quantity": 0},
#     "hdmi cable": {"price":20, "quantity": 7},
#     "dvd drive": {"price":50, "quantity": 5},
# }
# current_choice = None
# tottal_price = 0
# while current_choice != "0":
#     if current_choice in available_parts:
#         chosen_part = available_parts[current_choice]
#         if price_quantity[chosen_part]["quantity"] > 0:
#             # implement logic
#             print(f"Adding {chosen_part}")
#             price_quantity[chosen_part]["quantity"] -= 1
#             tottal_price += price_quantity[chosen_part]["price"]
#         else:
#             print(f"{chosen_part} is out of stock!.")
#     else:
#         print("Please add options from the list")
#         for key, value in available_parts.items():
#             print(f"{key}: {value}")
#         print("0: to finish")
#     current_choice = input("> ")
        
# print(f"Total Price: {tottal_price}")




# Project 28 Blind Auction Program
# from ascii_art import logo
# import os

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# print(logo)
# print("Welcome to my Python program!")

# def find_highest_amount(p_bid_record):
#     highest_bid = 0
#     highest_bidder = ""
#     for key, value in p_bid_record.items():
#         if value > highest_bid:
#             highest_bid = value
#             highest_bidder = key
#     print(f"\nThe winner is {highest_bidder} with a bid of ${highest_bid}")

# bids = {}
# bidding_finished = False

# while not bidding_finished:
#     name = input("What is your name?: ")
#     bid_amount = int(input("What is your bid amount? $"))  # convert to int
#     bids[name] = bid_amount
#     should_continue = input("Are there any other bidders? (Y/N): ").upper()
#     if should_continue == "N":
#         bidding_finished = True
#         find_highest_amount(bids)
#     elif should_continue == "Y":
#         clear()
    


# Project 29 Quiz App
# import os

# logo = """ 
#  ██████  ██    ██ ██ ███████      █████  ██████  ██████  
# ██    ██ ██    ██ ██    ███      ██   ██ ██   ██ ██   ██ 
# ██    ██ ██    ██ ██   ███       ███████ ██████  ██████  
# ██ ▄▄ ██ ██    ██ ██  ███        ██   ██ ██      ██      
#  ██████   ██████  ██ ███████     ██   ██ ██      ██      
#     ▀▀                                                  """

# print(logo)
# print("Welcome to the Quiz App")
# print("There are total of 6 questions, you can skip a question anytime by typing 'skip....")
        
# import os

# # Function to clear screen
# def clear():
#     os.system("cls" if os.name == "nt" else "clear")

# logo = "===== QUIZ APP ====="

# print("Welcome to the Quiz App")
# print("There are a total of 6 questions, you can skip a question anytime by typing 'skip'")

# quiz = {
#     1: {"question": "A mapping from a set of keys to their corresponding values", "answer": "Dictionary"},
#     2: {"question": "Another name for a key-value pair", "answer": "Item"},
#     3: {"question": "An object that appears in a dictionary as the first part of a key-value pair", "answer": "Key"},
#     4: {"question": "An object that appears in a dictionary as the second part of a key-value pair", "answer": "Value"},
#     5: {"question": "A loop “inside” of another loop.", "answer": "Nested Loop"},
#     6: {"question": "A dictionary that is an element of another dictionary", "answer": "Nested Dictionary"}
# }

# def check_ans(question, ans, attempts, player):
#     clear()
#     if quiz[question]['answer'].lower() == ans.lower():
#         print(f"✅ Correct Answer! \n{player}'s score is {player_score[player] + 1}!")
#         return True
#     else:
#         print(f"❌ Wrong Answer :( \nYou have {attempts - 1} attempts left. Try again...")
#         return False

# def print_dictionary():
#     for q_id, qa in quiz.items():
#         print(f"Q{q_id}: {qa['question']} -> {qa['answer']}")

# def intro_message():
#     print(logo)
#     print("There are a total of 6 questions, you can skip a question anytime by typing 'skip'")
#     input("Press Enter to get started...")
#     return True

# def switch_users(idx):
#     return 1 - idx   # flip between 0 and 1

# def print_winner(p1, p2):
#     if player_score[p1] > player_score[p2]:
#         print(f"🎉 {p1} WON! Final score: {player_score[p1]}")
#     elif player_score[p1] < player_score[p2]:
#         print(f"🎉 {p2} WON! Final score: {player_score[p2]}")
#     else:
#         print("🤝 It's a DRAW!")

# # Main Game
# intro_message()
# players = input("Enter 2 Players (separated by space): ").split()
# if len(players) < 2:
#     print("Need 2 players to play! Exiting...")
#     exit()

# player_score = dict.fromkeys(players, 0)
# current_index = 0

# for q in quiz:
#     print("------------------------------")
#     current_player = players[current_index]
#     print(f"It is {current_player}'s turn.")
#     attempts = 2
#     while attempts > 0:
#         print(quiz[q]['question'])
#         answer = input("Enter Answer (or type 'skip' to move on): ")
#         if answer.lower() == "skip":
#             break
#         if check_ans(q, answer, attempts, current_player):
#             player_score[current_player] += 1
#             break
#         attempts -= 1
#     current_index = switch_users(current_index)

# print_winner(players[0], players[1])

# correct_answer = input("Do you want to see the correct answers? (Y/N): ")
# if correct_answer.lower() == "y":
#     print_dictionary()

# print("🎮 Thanks for playing!")


# List in python
# cust_info = ['Satyajit pattnaik', 57, 1200]
# type(cust_info)
# print(cust_info)

# nested list
# list1 =['india', 'usa', 5,6, ['russia', 'china']]
# len(list1)
# print(len(list1))

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list3 = list1+list2
# print(0 in list1)
# print(list3)
# list1.pop(1)
# list1.extend([10,11])
# list1.append([20,30])
# list2.sort()
# print(list2)

# Tuple in Python
'''tuple is a data structure with round brackets like (1,2,3)'''
'''list is a data structure with square brackets like [1,2,3]'''
'''dictionary is a data structure with curly brackets like {1,2,3}'''
# my_tuple = (1,2,3,4)
# my_tuple = tuple('hello')
# print(my_tuple) # same result
# print((1,2,3,4)) # same result
# print(type(my_tuple))
# print(my_tuple)


# club = ("FC Barcelona", "Spain", 1899)
# # print(club)
# # print(club[0])
# # print(club[1])
# # print(club[2])
# # club[0] = "Real Madrid" # error because tuples are immutable and are less memory
# club2 = list(club)
# print(club2)
# club2[0] = "Real Madrid"
# club2[2] = 1999
# print(club2)




# a=b=c=d=20
# a=10
# b=10
# c=10
# d=10
# x,y,z = 10,20,30
# print("Unpacking tuple")
# my_tuple = {10,20,30}
# x,y,z = my_tuple
# print(my_tuple)
# print(x)
# print(y)
# print(z)

# print("Unpacking lis")
# my_list = (40,50,60)
# a,b,c = my_list
# print(my_list)



# coding exercise solution of sum of tuple elements using UNPACK
# my_tuple = (10,40,80,90)
# a,b,c,d = my_tuple
# print(f"{a}+{b}+{c}+{d}={a+b+c+d}")




# Traverse tuple - Enumerate()
# my_tuple = ("one", "two", "three")
# my_list = [1,2,3,4]
# for index, value in enumerate(my_tuple):
#     print(index, value)
    
    

# coding exercise even index with enumerate
# my_tuple = ("a", "b", "c", "d", "e", "f", "g")
# def even_index_items(p_tuple):
#     result_list = []
#     for index, value in enumerate(p_tuple):
#         if index % 2 == 0:
#             result_list.append(value)
#     result_list = tuple(result_list)
#     return result_list
# result_tuple = even_index_items(my_tuple)
# print(result_tuple)


# t1 = (1,2,3,'hello', 'tuple')
# print(len(t1))
# print(type(t1))
# t2 = (1,2,3,(4,5))
# t1 = 1,2,3,4
# print(t2)
# print(t1)
# print(type(t1))
# print(type(t2))
# t = ('mumbai', 10, 'python', 100)
# print(t[2:])
# print(t[0:3])
# print(t[-2:-2])
# print(t[1:1])


# list1 = ('Hello!', "Welcome", 5,10,'math')
# list1[2] = 'computer'
# print(list1)

# t1 = ("Hello", "welcome", 5,10, "world", "of", "analytics")
# print(t1[0:2])
# print(t1[-3:])
# t3 = t1[0:2] + ("to", "the") + t1[-3:]
# print(t3)

# t=(1,5,"hello", "world", ("java", "python"))
# print(t[4:0])
# print(t[4:-2])

# ----------------------------------------------------------
# sets in python
# list1 = [1,2,3,4,5]
# set1 = set(list1)
# # print(type(set1))
# set1.add('python')
# print(set1)

# a= {1,2,3,4}
# b={5,6,7,8}
# print(a | b)
# print(a.union(b))
# set1 = set(a) & set(b)
# print(set1)
# print(sorted(a))
# print(a.intersection(b))


# Dictionary in python
# dictinoary = {"key": "value"}
# d1 = {"name": "John", "age": 18}
# print(type(d1))
# print(d1)

# d1 = {"India": "inr", "USA": "usd", "Hong Kong": "hkd", "Japan": "Yen"}
# print(d1["India"])
# d1["Hong Kong"]= "Yen"
# print(d1)
# del d1["Hong Kong"]
# print(d1)
# print(d1.values())
# print(d1.keys())
# employee_data = {101:['John', 24, 'Content Creater'], 102:['Alex', 59, "Software Engineer"]}
# print(employee_data[101][2])

# input_dict = {'Name': 'Monty', 'Profession': 'Singer'}
# # input_dict["Age"]
# if "Label" in input_dict.keys():
#     print(input_dict["label"])
# else:
#     print("NA")

# d1 = {'Jack Dorsey': 'Twitter', 'Tim Cook': 'Apple', 'Jeff Bezos': 'Amazon'}
# print(sorted(d1.values()))
# print(d1)
# print(sorted(d1.keys()))



# Loops and Iterations
# x = int(input("Enter Number"))
# if x%2==0:
#     print("even")
# else:
#     print("odd")


# age = int(input("Enter your age: "))
# if age > 18:
#     print("you are eligible to drive")
# else:
#     print("you are not eligible to drive")
    


# shopiing_cart = int(input("Input your billing amount: "))
# if shopiing_cart >= 50000:
#     print("Yhave 50000..")
# elif shopiing_cart >= 25000:
#     print("you have 25$")
# else:
#     print("you dont have.")

# list1 = [1,2,3,4]
# for i in list1:
#     print(i)


# str1 = "python"
# for i in str1:
#     print(i)

# std_data = {
#     1: ["Sam", 25],
#     2: ["Sharma", 30],
#     3: ["Ravi", 50]
# }

# for i in std_data.items():
#     print(i)


# std_data = {
#     1: ["Sam", 25],
#     2: ["Sharma", 30],
#     3: ["Ravi", 50]
# }

# for i,j in std_data.items():
#     print(j)

# list1 = ["BMW", "BENZ", "MG"]
# list2 = []
# for i in list1:
#     list2.append(list1)
# print(list2)

# list1 = ["BMW", "BENZ", "MG"]
# d = {i: len(i) for i in list1}
# print(d)




#  Functions
# factorial function
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factorial(5))


# sum of natural numbers
# def sum(n):
#     num=0
#     for i in range(1,n+1):
#         num+=i
#     return num
# print(sum(5))

# Lambda
# lambda argument: expressions
# x=lambda a: a+10
# print(x(25))

# x=lambda a: "even" if a % 2 == 0 else "Odd"
# print(x(11))


# x=lambda a,b: a*b
# print(x(2,3))


# import math
# def area(r):
#     return math.pi*(r**2)
# radii = [1,2,3,4,5]
# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)
# print(area(2))


# map function
# map(area, radii)

# temps = [("Mumbai", 35), ("Berlin", 12), ("Tokyo", 20)]
# type(temps)
# len(temps)
# cel_to_f = lambda data: (data[0], (9/5)*data[1]+32)
# print(list(map(cel_to_f, temps)))


# filter function
# import statistics
# data = [1,2,3,4,5,6,7,8,9]
# avg = statistics.mean(data)
# print(avg)

# list(filter(lambda x: x> avg, data))


# name = ["Sam", "Ravi", 0, 0.0, "Alex"]
# print(filter(None, name))


# reduce function
# import math
# data = [1,2,3,4,5,6]
# multiplier = lambda x,y: x*y
# reduce(multiplier, data)



# file handling
# file = open('one.txt', 'r')
# print(file.read())


# file = open('one.txt', 'w')
# file.write("This is some lines")
# file.close()

# file = open('test.txt', 'r')
# print(file.read())


# file = open('one.txt', 'a')
# file.write("This is some lines")
# file.close()


# OOP in python
# class rectangle:
#     def __init__(self):
#         self.length = 10
#         self.breadth = 5
# rect = rectangle()
# print(rect.length)
# print(rect.breadth)


# # parameterized constructor
# class rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
# rect = rectangle(5,10)
# print(rect.breadth)



# class and instance variable
# class rectangle:
    # pi = 3.14
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
# rect = rectangle(5,10)
# print(rect.breadth)


# add method/function
# class rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def calculate(a, b):
#      return a+ b
# rect = rectangle(5,10)
# print(rect.breadth)
        
        
# Inheritance and overriding
# class employee:
#     def fun1(self):
#         print("helo from employee")

# class department(employee):
#     pass
# emp = employee()
# print(emp.fun1())


class shape:
    def set_color(self, color):
        self.color = color
        
    def calarea(self):
        pass
    def colortheshape(self):
        color_price = {"red", 10, "blue", 15}
        return self.calarea() * color_price[self.color]
    
# class circle(shape):
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
        
#     def calculatearea(self):
#         return circle.pi * self.radius
# c = circle()
# c.set_color("red")
# print("circle with radius= ", c.radius, "when colored ", c.color, "cost $", c.colortheshape)