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
Avg = sum(var / len(var))
print(Avg)
varr = x['Salary(USD)']
v = without_dup['Salary(USD)'] = varr.median()
print("The Median Salaries")
print(v)
print("Ration between males and female employees")
num_males = sum(without_dup['Gender'] == 'M')
num_females = len(without_dup['Gender']) - num_males
print(f"M : {len(without_dup[without_dup['Gender'] == 'M'])}")
print(f"F : {len(without_dup[without_dup['Gender'] == 'F'])}")

with open('/Users/user/Downloads/new_Employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Average age", "Median Salaries", "num_females", 'num_males'])
    writer.writerow([Avg, v, num_females, num_males])
