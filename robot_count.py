# prompt the user to enter the number of obstacle to avoid
num_obstacles_to_avoid = int(input("How many obstacles must I avoid"))

# Initialize the variable to track the number of avoided obstacles.
num_obstacles_avoid = 0

# Create a while loop to avoid obstacles.
while num_obstacles_avoid < num_obstacles_to_avoid:

    # Display the message "Avoiding..." at the start of each iteration.
    print("Avoiding...")

    # Increment the variable for trucking the number of obstacles
    num_obstacles_avoid += 1

    # Display the message "...Done! [n] obstacles avoided!" at the end of each iteration.
    print(f"...Done! {num_obstacles_avoid} obstacles avoided!")

# Display the message "All obstacles have been avoided."
print("All obstacles have been avoided!")
