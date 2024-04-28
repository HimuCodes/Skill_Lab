# Generating a list of tuples containing name, age, and salary

def generate_tuples(names, ages, salaries):
    """Generates a list of tuples containing name, age, and salary."""
    return list(zip(names, ages, salaries))

# Sample data
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
salaries = [50000, 60000, 70000]

# Generating tuples
data = generate_tuples(names, ages, salaries)

print("\nList of tuples containing name, age, and salary:")
print(data)

# Separating names, ages, and salaries
all_names = tuple(name for name, _, _ in data)  # Using unpacking
all_ages = tuple(age for _, age, _ in data)   # Using unpacking
all_salaries = tuple(salary for _, _, salary in data)  # Using unpacking

print("\nTuple containing all names:", all_names)
print("Tuple containing all ages:", all_ages)
print("Tuple containing all salaries:", all_salaries)
