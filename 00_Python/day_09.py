import pandas 

df = pandas.read_csv('churn_data.csv')

# print(df.columns)
# print(df.info())

# df.rename({
#     'Monthly Charge':'MonthlyCharge',
#     'Age':'age'
# },axis=1,inplace=True)

# print(df.columns)

# print(df.Age.min())



# print(type(df))

# select top 10 * from table
# print(df.head())
# print(df.tail())

# select age, monthly_charges from df

# col = ['Age','MonthlyCharge']
# print(type(df[col]))
# print(df[col].head())

# how to select the specific columns
# print(type(df.Age))
# print(df.Age.head())

# print(df['Monthly Charge'].head())

# output = df.describe()
# output.to_csv('stats.csv')
# print(output)

result = df.groupby('Churned').agg({
    'Monthly Charge':['mean','min','max'],
    
})
print(result)

#   Age  Monthly Charge     Churned
# count  199.000000      200.000000  200.000000
# mean    47.693467       56.777250    0.050000
# std     13.022184       10.764798    0.218492
# min     25.000000       40.060000    0.000000
# 25%     36.000000       48.535000    0.000000
# 50%     48.000000       55.910000    0.000000
# 75%     59.500000       63.692500    0.000000
# max     70.000000       94.630000    1.000000