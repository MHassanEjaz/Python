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
list = [1,2,3,4,5]
for val in list:
    print(val)