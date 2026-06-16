

# ### intermediate_questions.py


# # =====================================
# # INTERMEDIATE PYTHON PRACTICE QUESTIONS
# # =====================================

# # -------------------------------------
# # LIST COMPREHENSIONS
# # -------------------------------------

# # Q1 Create a list containing squares of numbers from 1 to 10.
# square=[i**2 for i in range(1,11)]
# print(square)

# # Q2 Create a list of even numbers from 1 to 20.
# even=[i for i in range(1,21) if i %2==0]
# print(even)

# # Q3 Create a list of lengths of each word in:
# # ["python", "backend", "developer"]
# word= ["python", "backend", "developer"]
# length=[len(l) for l in word]
# print(length)

# # Q4 Convert the following loop into a list comprehension:
# #
# #result = []
# #for i in range(1, 11):
#  #   result.append(i * 2)
# result = [i * 2 for i in range(1, 11)]

# # Q5 Create a list containing vowels from a given string.
# string="life is beautiful"
# vows=[i for i in string if i in "AEIOUaeiou"]
# print(vows)
# # -------------------------------------
# # LAMBDA FUNCTIONS
# # -------------------------------------

# # Q6 Create a lambda function that returns the square of a number.
# square=lambda x : x**2
# print(square(10))

# # Q7 Use lambda with map() to double all values in:
# # [1, 2, 3, 4, 5]

# nums=[1, 2, 3, 4, 5]
# result=list(map(lambda x:x*2,nums))
# print(result)

# # Q8 Use lambda with filter() to get even numbers from:
# # [1, 2, 3, 4, 5, 6, 7, 8]

# nums=[1, 2, 3, 4, 5, 6, 7, 8]
# even=list(filter(lambda x:x%2==0,nums ))
# print(even)

# # Q9 Sort the following list of tuples by age:
# # [("Ravi", 25), ("Aman", 22), ("Priya", 28)]

# lst=[("Ravi", 25), ("Aman", 22), ("Priya", 28)]
# lst.sort(key=lambda x:x[1])
# # Q10 Sort words by their length using lambda.
# word=['hello','world']
# word.sort(key=lambda x: len(x))
# print(word)
# # -------------------------------------
# # *ARGS AND **KWARGS
# # -------------------------------------

# # Q11 Write a function that accepts any number of integers
# # and returns their sum using *args.
# def add(*args):
#     return sum(args)
# print(add(5,20,15,10))

# # Q12 Write a function that prints all values passed through *args.
# def all_val(*args):
#     return args
# print(all_val(20,30,40,"hello"))
# # Q13 Write a function that accepts any number of keyword
# # arguments and prints key-value pairs.
# def keys(**kwargs):
#     print (kwargs)

# keys(name="rutu",age=25)




# # Q14 Create a function:
# # greet(name, *args)
# def greet(name,*args):
#     print (f"{name} hello mate ,{args}")
# greet("ruturaj",30,40,50)

# # Q15 Create a function:
# # profile(**kwargs)
# def profile(**kwargs):
#     print(kwargs)

# profile(name="ruturaj",age=30)
# # -------------------------------------
# # EXCEPTION HANDLING
# # -------------------------------------

# # Q16 Handle ZeroDivisionError.
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(f"{e} ,cant divide by 0")


# # Q17 Handle ValueError when converting input to integer.
# try:
#     inp=int(input("enter word:-"))
# except ValueError as e:
#     print(f"{e}, cant convert word to int")

# # Q18 Use try-except-else-finally.
# try:
#     print(10/2)
# except ZeroDivisionError as e:
#     print(f"{e} , can't divide by zero")
# else:
#     print("success")
# finally:
#     print('close program')

# # Q19 Raise a custom exception if age is less than 18.
# age=int(input("enter age:-"))
# if age<18:
#     raise ValueError("age must be 18+")

# # Q20 Create a custom exception class called InvalidAgeError.

# class InvalidAgeError(Exception):
#     pass

# age = int(input())

# if age < 18:
#     raise InvalidAgeError("Age must be 18+")

# # -------------------------------------
# # FILE HANDLING
# # -------------------------------------

# # Q21 Create a file and write your name into it.

# with open ("rvd.txt","w")as file:
#     data=file.write("hello rvd")

# # Q22 Read data from a file.
# with open ("rvd.txt","r")as file:
#     data=file.read()
# # # Q23 Append a new line into an existing file.
# with open ("rvd.txt","a")as file:
#     data=file.write("\n hello world")
# # Q24 Count the number of lines in a file.
# with open("rvd.txt","r")as file:
#     data=file.readlines()

# # Q25 Count the number of words in a file.
#dont know

# # Q26 Read a file using with open().
# with open("rvd.txt","r")as file:
#     data=file.read()

# # -------------------------------------
# # JSON HANDLING
# # -------------------------------------

# Q27 Convert a Python dictionary into JSON.
# import json
# dic={'name':"ruturaj","age":25}
# json_data=json.dumps(dic)
# print(json_data)

# # Q28 Convert JSON string into Python dictionary.
# import json
# json_str= '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
# dictionary=json.loads(json_str)
# print(dictionary)

# # Q29 Store employee data in a JSON file.
# import json
# with open("emp.json",'w') as file:
#     json.dump("data",file)
# # Q30 Read employee data from a JSON file.
# import json
# with open("emp.json","r") as file:
#     json.load(file)

# # Q31 Create a JSON file containing:
# # name, age, city
# import json

# data = {
#     "name": "John wick",
#     "age": 30,
#     "city": "New York"
# }

# with open('data.json', 'w') as file:
#     json.dump(data, file)

# # # Q32 Load JSON data and print only names.
# import json
# with open ("data.json","r") as file:
#     json.load(file)

# # -------------------------------------
# # MINI CHALLENGES
# # -------------------------------------

# # Q33 Read a text file and count total words.

# # Q34 Read a JSON file containing students and print
# # students with marks above 80.

# # Q35 Create a function that accepts *args and returns
# # the largest value.

# # Q36 Create a lambda function to sort a list of
# # dictionaries by age.

# # Q37 Create a file named log.txt and append logs
# # every time the program runs.

# # Q38 Handle FileNotFoundError gracefully.

# # Q39 Convert a list of names into uppercase using map().

# # Q40 Create a JSON file storing 5 products and read it back.

# # =====================================
# # END OF INTERMEDIATE PRACTICE SET
# # =====================================