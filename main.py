import pandas as pd
import csv

x = pd.read_csv('/Users/user/Downloads/Employees.csv')
without_dup = x.drop_duplicates()
print(without_dup)
without_dup['Age'] = without_dup['Age'].round(0)
print("The Age Without Decimal Point:")
print(without_dup)
var = without_dup['Age']
print('The Average Of Age: ')
print(sum(var / len(var)))
varr = without_dup['Salary(USD)']
v = without_dup['Salary(USD)'] = varr.median()
print("The Median Salaries")
print(v)
print("Ration between males and female employees")
print(f"M : {len(without_dup[without_dup['Gender'] == 'M'])}")
print(f"F : {len(without_dup[without_dup['Gender'] == 'F'])}")

file = open('/Users/user/Downloads/Employee.csv')
writer = csv.writer(file)
writer.writerows(without_dup)
file.close()
