# Prompt the user to enter a word.
word = input("What word do you see? ")

# Create a variable to store the index position of the character.
index = 0

# Use a for loop to display each character in the user's response along with its index position on a new line.
for char in word:
    print(f"Character at index {index}: {char}")
    index += 1
