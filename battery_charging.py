# Prompt the user to enter the number of bars to charge.
num_bars_to_charge = int(input("How many bars should be charged? "))

# Initialize the variable to track the number of charged bars.
num_bars_charged = 0

# Create a while loop to charge the battery.
while num_bars_charged < num_bars_to_charge:

    # Display the message "Charging:".
    print("Charging:")

    # Increment the variable for tracking the number of charged bars.
    num_bars_charged += 1

    # Display the number of charged bars.
    print(f"{num_bars_charged} bars charged.")

# Display the message "The battery is fully charged."
print("The battery is fully charged.")
