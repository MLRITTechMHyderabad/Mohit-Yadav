# name = string(input("name"))
# salary  = float(input("float"))
# rating = int(input("number"))
employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

# Function to apply salary adjustment
adjust_salary = lambda emp: {
    **emp, 
    "salary": round(emp["salary"] * (1.1 if emp["rating"] in [4, 5] else 1.05 if emp["rating"] == 3 else 0.97), 2)
}

# Apply the salary adjustment using map
updated_employees = list(map(adjust_salary, employees))

# Print the updated list
print(updated_employees)
