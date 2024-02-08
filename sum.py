# Prompt the user to enter the number till they want to count.
num = int(input("Please enter the number till you want to count: "))

# Start calculating the sum of the first (specific number entered by user) numbers from 1.

Sum = 0
for i in range(1, num + 1):
    sum += i

# Display the answer.
print(f"...Done! The answer is {sum}.")
