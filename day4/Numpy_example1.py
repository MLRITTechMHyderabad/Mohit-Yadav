import numpy as np
resources = np.random.randint(15, 51, (6, 3))
total_resources = np.sum(resources, axis=0)
print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water: {total_resources[1]}, Food: {total_resources[2]}")

max_per_month = np.max(resources, axis=1)
max_total = np.max(total_resources)
max_total_resource = ["Oxygen", "Water", "Food"][np.argmax(total_resources)]
max_month = np.unravel_index(np.argmax(resources), resources.shape)[0] + 1
max_resource = ["Oxygen", "Water", "Food"][np.argmax(resources[max_month - 1])]
max_value = np.max(resources)
print(f"Highest consumption in a month: {max_resource} ({max_value} tons in month {max_month})")

std_dev = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_dev[0]:.2f}, Water: {std_dev[1]:.2f}, Food: {std_dev[2]:.2f}")

transposed_matrix = resources.T
print("Transposed matrix:")
print(transposed_matrix)