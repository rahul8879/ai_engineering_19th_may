import pandas as pd

df = pd.read_csv('churn_data.csv')
# print(df.shape)
# print(df.head())

# df_2 = df[( df['Churned'] == 1)]  # select * from table where churned = 1 and age > 24
# print(df_2.head())
# print(df_2.shape)
# print('avg monthly charge is for churned ',df_2['Monthly Charge'].mean())

# df_3 = df[( df['Churned'] == 0)]  
# print(df_3.head())
# print(df_3.shape)
# print('avg monthly charge is for not churned ',df_3['Monthly Charge'].mean())
# output = df.groupby('Churned')['Monthly Charge'].mean()
# age_output = df.groupby('Churned')['Age'].mean()
# print(output)
# print(age_output)

# output = df.groupby('Churned').agg({
#     'Monthly Charge': ['mean','sum'],
#     'Age': ['mean','min']
# })
# print(output)

#         Monthly Charge        Age
# Churned                           
# 0             55.261211  47.608466
# 1             85.582000  49.300000



# Churned
# 0    55.261211
# 1    85.582000


# data = {
#     'product_name': ['A','A','C','A','E'],
#     'sales': [200,300,400,500,600],

# }

# sales_df = pd.DataFrame(data)
# print(sales_df.head(2))

# print(sales_df.groupby('product_name')['sales'].mean())


import numpy as np

x = np.random.randint(1,100,20)
# print(x)
catgegories = ['A','B','C','D','E']
sub_catgegories = ['A1','A2','A3','A4','A5']
y = np.random.choice(catgegories,20)
# print(y)


data = {
    'catgegory': np.random.choice(catgegories,20),
    'sub_catgegory': np.random.choice(sub_catgegories,20),
    'sales': np.random.randint(1,100,20)

}

# find the avg sales for each category ?? code 


# sales_df = pd.DataFrame(data)
# print(sales_df.head(2))

# print(sales_df.groupby(['catgegory','sub_catgegory'])['sales'].sum())
# select 



#         catgegory sub_catgegory  sales
# 0         B            A2     41
# 1         C            A3     41
# catgegory  sub_catgegory
# A          A4                48
#            A5               127
# B          A1                41
#            A2                41
#            A3                 2
# C          A1                82
#            A2                10
#            A3                41
#            A4                53
#            A5                32
# D          A5                32
# E          A2               122
#            A3                83
#            A5               139

df = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3", "K4", "K5"],
        "A": ["A0", "A1", "A2", "A3", "A4", "A5"],
    }
)

other = pd.DataFrame({"key": ["K0", "K1", "K2"], "B": ["B0", "B1", "B2"]})
print(df.head())
print(other.head())

# table A
#  key   A
# 0  K0  A0
# 1  K1  A1
# 2  K2  A2
# 3  K3  A3
# 4  K4  A4

# table 2 :
#   key   B
# 0  K0  B0
# 1  K1  B1
# 2  K2  B2

# df_merged = df.join(other, lsuffix='_table_1', rsuffix='_table_2', how='left')
# print(df_merged)

result = df.merge(other, how='left', on='key')

print(result)