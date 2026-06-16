# marks = [85, 90, 78, 92, 88]
data = (23,26,27,(23,25),[24,25])
# print(type(data))
# data[0] = 24
# data[-1][0] = 34
# print(data[-1])


# you cant change the elements of tuple but if 
# elements are the mutable type then you can change the elements of the tuple

# access the elements
# del marks[0:2]
# modify the elements
# marks[0] = 101
# marks[1] = [2,3,4]
# print(marks)
# second_mark = marks[1]
# third_mark = marks[2]
# fourth_mark = marks[3]
# fifth_mark = marks[-1]

# print(first_mark, second_mark, third_mark, fourth_mark, fifth_mark)

number = [2,3,4,5,6]
# even= []
# for num in number:
#     if num%2 == 0:
#         even.append(num)
# print(even)

# even = [i for i in number if i%2 == 0]
# print(even)


# fruits = ['apple', 'banana', 'mango','orange','grape']
sales_data=[100, 150, 200, 250, 300,400,450]

odd_sales = sales_data[0::2]
even_sales = sales_data[1::2]

# odd_sales_avg = sum(odd_sales) / len(odd_sales) 
# even_sales_avg = sum(even_sales) / len(even_sales)
# print("Average of odd sales:", odd_sales_avg)
# print("Average of even sales:", even_sales_avg)

# marks = [85, 90, 78, 92, 88]
# print(marks)
# marks.append(95)
# print(marks)
# marks.insert(2, 80)
# print(marks)

# new_student = [88, 92, 95]
# marks.append(new_student)
# print(marks)

# marks.extend(new_student)
# print(marks)

# result = marks.count(88)
# print(result)

# marks.sort(reverse=True)
# print(marks)
# del marks
# print(marks)



cart = []

product={
   "product":"banana",
   "price":0.99
}

product_2={
   "product":"apple",
   "price":26
}

product_3={
   "product":"orange",
   "price":30
}

cart.append(product)
cart.append(product_2)
cart.append(product_3)
print(cart)
# print(product_3['test'])
total_price = 0
for i in cart:
    total_price = total_price + i['price']
print("Total price:", round(total_price,2))