# Prompt the user to enter the number of numbers to sum up.
num_numbers = int(input("How many numbers should I sum up? "))

# Initialize the running total.
Sum = 0

# Use a while loop to repeatedly prompt the user for a number and add it to the running total.
while num_numbers > 0:
    number = int(input(f"Enter a number "))
    sum += number
    num_numbers -= 1

# Display the answer.
print(f"The answer is {sum}.")
