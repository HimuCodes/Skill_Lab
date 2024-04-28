def check_odd_even(num):
    """Checks if a number is odd or even and returns a string."""
    try:
        if num % 2 == 0:
            return f"{num} is even"
        else:
            return f"{num} is odd"
    except ValueError:
        return "Please enter a valid integer."

# Get user input and handle potential errors
while True:
    try:
        num = int(input("Enter an integer: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the check_odd_even function
result = check_odd_even(num)

print(result)
