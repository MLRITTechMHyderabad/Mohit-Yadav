import pandas 
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]

}

df = pandas.DataFrame(data)
print(df)
avg = df.groupby("Department")["Salary"].mean()
print(avg)

high = df.groupby("Department")["Salary"].max()
print(high)

count = len(df[(df["Experience"]> 5) & (df["Salary"] > 65000)])
print(count)

def seniority(exp):
  if exp < 5:
    return "Junior"
  elif   5< exp < 10:
    return "Mid- level"
  else:
    return " Senior"
df["Seniority"] = df["Experience"].apply(seniority)
print(df)

print(df[df["Department"] == "IT"].sort_values(by = "Salary", ascending = False))



# 1.	Find the average salary of employees in each department.
# 2.	Find the highest-paid employee in each department.
# 3.	Determine how many employees have more than 5 years of experience and earn a salary above $65,000.
# 4.	Add a new column “Seniority”:
# –	“Junior” (Experience < 5 years)
# –	“Mid-Level” (Experience between 5-10 years)
# –	“Senior” (Experience > 10 years)
# 5.	Sort employees by salary in descending order, showing only “IT” department employees.
