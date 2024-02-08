# Prompt the user to enter the number of rows and columns they would like.
num_rows = int(input("How many rows would you like? "))
num_columns = int(input("How many columns would you like? "))

# Create a list of ASCII emoji.
emoji = ["😀", "😄", "😁", "😆", "😅"]

# Use a nested for loop to display a grid of ASCII emoji.
for row in range(num_rows):
    for column in range(num_columns):
        # Display the emoji at the current row and column index.
        print(emoji[(row + column) % len(emoji)], end=" ")

    # Print a newline character at the end of each row.
    print()
