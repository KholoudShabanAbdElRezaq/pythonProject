import pandas as pd
import csv

x = pd.read_csv('/Users/user/Downloads/Employees.csv')
without_dup = x.drop_duplicates()
print(without_dup)
without_dup['Age'] = without_dup['Age'].round(0)
print("The Age Without Decimal Point:")
print(without_dup['Age'])
print(without_dup)
f = without_dup['Salary(USD)'] * 30.9
print('The Convert the USD salary to EGP')
print(f)
var = without_dup['Age']
print('The Average Of Age:')
print(sum(var / len(var)))
varr = x['Salary(USD)']
v = without_dup['Salary(USD)'] = varr.median()
print("The Median Salaries")
print(v)
print("Ration between males and female employees")
print(f"M : {len(without_dup[without_dup['Gender'] == 'M'])}")
print(f"F : {len(without_dup[without_dup['Gender'] == 'F'])}")


without_dup.to_csv('/Users/user/Downloads/new_Employees.csv')
