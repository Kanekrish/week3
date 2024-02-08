# Create a list of ASCII mountains.
mountains = """
    /\
   /  \
  /    \
 /      \
"""


# Prompt the user to enter the number of mountains to display.
num_mountains = int(input("How many mountains should I display? "))

# Use a for loop to display the specified number of ASCII mountains.
for i in range(num_mountains):
    print(mountains)
