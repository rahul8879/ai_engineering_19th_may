# # age = True
# # print(type(age))

# # call_llm = True
# # print(type(call_llm)) # here type() --> it will return the tyoe of your variables

# # data = [24,26,27,28,'rahul']
# # print(type(data))
# # print(type(data[0]))


# # rules 
# # 3_age = 24
# # age = 34
# # while = 34
    
# # reserved keywords : 
# import keyword
# print(keyword.kwlist) # it will return the list of reserved keywords in python

# # name = float('45.5')
# # age = 24
# # result = name+ age
# # print(result)


# # print(float('65.8'))

# # print((7/3))
# # # print(6%3)
# # print(7 // 3)

# # pydantic  : it will help you to define or restrict the data types

# # age = input("Enter your age: ")
# # updated_age = int(age) + 1
# # print("Your age after one year will be: ", updated_age)


# data = [24, 26, 27, 28]

# print(len(data)) # it will return the length of the list
# print(sum(data)/len(data)) # it will return the sum of the list

# prompt = """Please help me to get the answer of below questions:
# {questions} 

# """
# print(len(prompt)) # it will return the length of the string'
# print(prompt[0])


age = 18

# if age>24:
#     test= 3
#     print("You are above 24 years old")
#     print("You are eligible to vote.")
#     print("You can also drive a car.")
# else:
#     print("You are not eligible to vote.")
#     print("You cannot drive a car.")


# if age < 24:
#     test = 2
#     print("You are below 24 years old")
#     print("You are not eligible to vote.")
#     print("You cannot drive a car.")

# elif age == 24:
#     test = 1
#     print("You are exactly 24 years old")
#     print("You are eligible to vote.")
#     print("You can also drive a car.")
# elif age > 24:
#     test = 4
#     print("You are above 24 years old")
#     print("You are eligible to vote.")
#     print("You can also drive a car.")

# else:
#     test = 0
#     print("You are below 24 years old")
#     print("You are not eligible to vote.")
#     print("You cannot drive a car.")


data = ['rahul','test','byte','testing']

# for i in data:
#     if i =='byte':
#        print("Found byte")
#        break
#     print(i)


for i in range(len(data)):
    if data[i] == 'byte':
       print("Found byte at index", i)
       break
    print(data[i])



