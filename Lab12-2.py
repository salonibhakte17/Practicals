import pandas as pd

df = pd.read_excel("employee.xlsx")

print("Employees in Automotive Domain:")
print(df[df['Department'] == 'Automotive'])

emp_id = int(input("Enter Employee ID: "))
print("Employee Details:")
print(df[df['Employee ID'] == emp_id])

print("List of Developers:")
print(df[df['Designation'] == 'Developer'])