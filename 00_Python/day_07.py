# from openai import OpenAI
# from dotenv import load_dotenv

# print(load_dotenv())

# try:
#     client = OpenAI()
# except Exception as e:
#     print(e)


# # def call_llm(prompt):
# #     response = client.chat.completions.create(
# #         model="gpt-4",
# #         messages=[
# #             {
# #                 "role": "user",
# #                 "content": prompt
# #             }
# #         ]
# #     ).choices[0].message.content
# #     return response

# # prompt = "Hi, help me to understand AI"
# # # response = call_llm(prompt)
# # try:
# #     response = call_llm(prompt)
# #     print(response)
# # except Exception as e:
# #     print(e)

# # def check_even(number):
# #     if number % 2 != 0:
# #         raise ValueError("Number is not even: tesing error")
# #     else:
# #         return True

# # check_even(3)


# # lst = ['4',0,2]
# # for entry in lst:
# #     try:
# #         r = 1/(entry)
# #         print(r)
# #     except(ValueError):
# #         print("This is a ValueError.")
# #     except(ZeroDivisionError):
# #         print("This is a ZeroError.")
# #     except(TypeError):
# #         print("This issue because of type mismatch")
# #     except:
# #         print("Some other error")
   
    
# # print(dir(__builtins__))



# # function arguments
# # 1) Default Arguments
# # def greet(name,msg="Good Morning"):
# #     print(f"Hi {name}, {msg}")

# # greet("Rahul","Good Evening")

# # 2) Keyword Arguments

# # def greet(**kwargs):
# #     print(kwargs)
# #     if kwargs:
# #         print("Hello {0},{1}".format(kwargs['name'],kwargs['msg']))
# #         print("Age : {0}".format(kwargs['age']))
# #     else:
# #         print("No arguments passed")

# # greet(name="Rahul",msg="Good Evening",test=24)


# #3 : Arbitrary Arguments
# # def greet(*names):
# #     print(names)


# # greet("Rahul",3,"Rahul")
# # print(2,'rahul',3,'rbyteai')

# # eg
# def double(x):
#     return x*2

# # lst = [3,4,5]
# # for i in lst:
# #     print(double(i))


# # map, filter
# # map ? 
# # print(list(map(lambda x: x*2,lst)))
# lst = [1, 2, 3, 4, 5]

# def even(x):
#     if x % 2 == 0:
#         return x

# even = lambda x: x if x % 2 == 0 else None    

# print(even(3)) #even(3)

# # result = []
# # for i in lst:
# #     print(result.append(even(i)))

# # print(result)

# # print(list(filter(lambda x: x % 2 == 0,lst)))

# # test = lambda x,y: x+y 
# # print(test(3,4)) #test(3,4)



# f = open("dummy.txt") # r means read
# print(f.readlines())

# 'r' Open a file for reading. (default)
# 'w' Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x' Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a' Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't' Open in text mode. (default)
# 'b' Open in binary mode.
# '+' Open a file for updating (reading and writing)
import os
# f = open("dummy.txt","a")
# f.write("Hello World")

# os.rename("dummy.txt","test.txt")
# os.remove("test.txt")
# print(os.getcwd())
# data = open("simple_data.json")
# print(data.readlines())
# import pandas as pd
# data = pd.read_json("simple_data.json")
# print('data is ',data)
# print(data.groupby('product_category')['price'].mean())


# without using numpy
import numpy as np
x = np.random.normal(0,1,10000000000)
import time
start_time = time.time()
toal_sum = 0
for i in x:
    toal_sum += i

end_time = time.time()
print("Execution time:", end_time - start_time)

# using numpy
import numpy as np
x = np.random.normal(0,1,1000000)
import time
start_time = time.time()
toal_sum = np.sum(x)
end_time = time.time()
print("Execution time:", end_time - start_time)