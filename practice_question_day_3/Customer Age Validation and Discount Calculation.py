customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

# Filter customers eligible for a discount
eligible_customers = filter(lambda c: c["age"] <= 40, customers)

# Apply the discount using map()
apply_discount = lambda c: {
    **c,
    "total_purchase": round(c["total_purchase"] * (0.90 if 18 <= c["age"] <= 25 else 0.95), 2)
}

# Generate the final list with discounted purchases
discounted_customers = list(map(apply_discount, eligible_customers))

# Print the result
print(discounted_customers)
