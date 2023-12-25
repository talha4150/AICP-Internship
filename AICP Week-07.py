#!/usr/bin/env python
# coding: utf-8

# # Talha Ahmad AICP Week-07

# In[5]:


#Task-01

def setup_donation_system():
    # Input and store the names of three charities
    charity_names = [input("Enter name for Charity 1: "),
                     input("Enter name for Charity 2: "),
                     input("Enter name for Charity 3: ")]

    # Display the charity names with corresponding numbers
    print("Charities:")
    for i, name in enumerate(charity_names, start=1):
        print(f"{i}. {name}")

    # Input the customer's choice of charity
    while True:
        try:
            choice = int(input("Choose a charity (1, 2, or 3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input the value of the customer's shopping bill
    shopping_bill = float(input("Enter the shopping bill amount: $"))

    # Calculate the donation (1% of the shopping bill)
    donation = shopping_bill * 0.01

    # Initialize totals for each charity to zero
    charity_totals = [0, 0, 0]

    # Update the total for the chosen charity
    charity_totals[choice - 1] += donation

    # Output the results
    print(f"Donation of ${donation:.2f} recorded for {charity_names[choice - 1]}.")
    print("Charity Totals:")
    for i, total in enumerate(charity_totals, start=1):
        print(f"Charity {i}: ${total:.2f}")


# Test the function
setup_donation_system()


# In[4]:


#Task-02

# Function to record and total each donation
def record_and_total_donation(charity_names, charity_totals):
    # Input the customer's choice of charity
    while True:
        try:
            choice = int(input("Choose a charity (1, 2, or 3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input the value of the customer's shopping bill
    shopping_bill = float(input("Enter the shopping bill amount: $"))

    # Calculate the donation (1% of the shopping bill)
    donation = shopping_bill * 0.01

    # Update the total for the chosen charity
    charity_totals[choice - 1] += donation

    # Output the results
    print(f"Donation of ${donation:.2f} recorded for {charity_names[choice - 1]}.")
    print("Updated Charity Totals:")
    for i, total in enumerate(charity_totals, start=1):
        print(f"Charity {i}: ${total:.2f}")


# Example usage:

# Initialize charity names and totals
charity_names = ["Charity A", "Charity B", "Charity C"]
charity_totals = [0, 0, 0]

# Record and total a donation
record_and_total_donation(charity_names, charity_totals)


# In[ ]:


#Task-03


# Initialize charity names and donation totals
charities = ["Charity A", "Charity B", "Charity C"]
charity_totals = [0, 0, 0]

# Function to display charities and their totals
def display_totals():
    print("\nCharity Totals:")
    for i in range(3):
        print(f"{charities[i]}: ${charity_totals[i]:.2f}")
    grand_total = sum(charity_totals)
    print("\nGRAND TOTAL DONATED TO CHARITY: $%.2f" % grand_total)

# Input and record donations
while True:
    # Get charity choice from the user
    charity_choice = int(input("\nEnter charity choice (1, 2, 3) or -1 to show totals: "))

    # Check for exit condition
    if charity_choice == -1:
        display_totals()
        break

    # Validate charity choice
    if 1 <= charity_choice <= 3:
        # Get the shopping bill amount from the user
        shopping_bill = float(input("Enter the value of the customer's shopping bill: $"))

        # Calculate donation
        donation = shopping_bill * 0.01

        # Update charity total
        charity_totals[charity_choice - 1] += donation

        # Display donation details
        print(f"Donation of ${donation:.2f} recorded for {charities[charity_choice - 1]}")
    else:
        print("Invalid charity choice. Please choose 1, 2, 3, or -1 to show totals.")


# In[ ]:




