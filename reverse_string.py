# Prompt the user to enter a phrase.
phrase = input("What phrase do you want to see in reverse?")

# Create a variable to store the reversed phrase.
reversed_phrase = ""

# Use a for loop to iterate over the phrase in reverse order.
for i in range(len(phrase) - 1, -1, -1):
    # Add the current character to the reversed phrase.
    reversed_phrase += phrase


# Display the reversed phrase.
print(reversed_phrase)

