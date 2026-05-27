# import numpy

# x = numpy.random.randint(1, 100, 10000)
# x = list(x)

# import time

# start_time = time.time()
# # Some operations on x
# for i in x:
#     if i ==78:
#         print(i)


# end_time = time.time()
# print("Execution time:", end_time - start_time)

# marks = {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# # search

# print(marks.get('Alice','Not found')) # it will return the value of the key 'Alice'

# you can modify or add 
# marks['Alice'] = 78
# marks['rahul'] = 85
# print(marks)

# print(marks.values()) # it will return the values of the dictionary

students = {
    'Amit'   : {'scores': [85, 92, 78, 90], 'grade': None},
    'Priya'  : {'scores': [95, 88, 97, 93], 'grade': None},
    'Rahul'  : {'scores': [60, 72, 55, 68], 'grade': None},
    'Sneha'  : {'scores': [45, 50, 48, 52], 'grade': None},
}

for i,j in students.items():
    avg = sum(j['scores']) / len(j['scores'])
    students[i]['average'] = avg
    # print("Average marks of", i, ":", avg)
    if avg >= 90:
        students[i]['grade'] = '+A'
    elif avg >= 80:
        students[i]['grade'] = 'A'
    elif avg >= 70:
        students[i]['grade'] = 'B'
    elif avg >= 60:
        students[i]['grade'] = 'C'
    else:
        students[i]['grade'] = 'F'

# print(students)

def flat_value(student):
    value = []
    for i in students:
        value.append(students[i]['average'])
    return value

# print(flat_value(students))

ranked = sorted(flat_value(students), reverse=True)
print(ranked)

ranked = sorted(students.items(), key=lambda x: x[1]['average'], reverse=True)
print(ranked)

# print(students['Amit']['scores'])

# amit_marks = students['Amit']['scores']
# avg_marks = sum(amit_marks) / len(amit_marks)
# print("Average marks of Amit:", avg_marks)
# if avg_marks >= 90:
#     students['Amit']['grade'] = '+A'
# elif avg_marks >= 80:
#     students['Amit']['grade'] = 'A'
# elif avg_marks >= 70:
#     students['Amit']['grade'] = 'B'
# else:
#     students['Amit']['grade'] = 'C'

# print(students)

data_1 = {4,1,6,9,11}
data_2 = {3,4,1,6,10}

data_1[0] = 23
print(data_1.intersection(data_2)) 
