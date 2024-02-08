# Prompt the user to enter the desired brightness level.
brightness_level = int(input("What level of brightness is required? "))


# Use a for loop to display asterix symbols to represent the current light level.
for brightness in range(2, brightness_level+1, 2):
    print("*" * brightness)


    