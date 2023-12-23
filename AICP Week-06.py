#!/usr/bin/env python
# coding: utf-8

# # Talha Ahmad AICP Week-06

# In[ ]:


#TASK-01

# Constants
MIN_WEIGHT_GRAVEL_SAND = 49.9
MAX_WEIGHT_GRAVEL_SAND = 50.1
MIN_WEIGHT_CEMENT = 24.9
MAX_WEIGHT_CEMENT = 25.1

# Function to check the contents and weight of a single sack
def check_sack(contents, weight):
    # Check contents
    if contents not in ['C', 'G', 'S']:
        return "Invalid contents. Accepted values: C, G, S"

    # Check weight based on contents
    if contents == 'C' and not (MIN_WEIGHT_CEMENT < weight < MAX_WEIGHT_CEMENT):
        return "Invalid weight for cement sack. Weight should be between 24.9 and 25.1 kilograms"
    elif contents in ['G', 'S'] and not (MIN_WEIGHT_GRAVEL_SAND < weight < MAX_WEIGHT_GRAVEL_SAND):
        return "Invalid weight for gravel or sand sack. Weight should be between 49.9 and 50.1 kilograms"

    # If all checks pass, return accepted sack details
    return f"Sack accepted - Contents: {contents}, Weight: {weight} kilograms"

# Input data
contents_input = input("Enter contents of the sack (C for cement, G for gravel, S for sand): ").upper()
weight_input = float(input("Enter weight of the sack in kilograms: "))

# Check and output results
result = check_sack(contents_input, weight_input)
print(result)


# In[22]:


#Task-02

# Constants
MIN_WEIGHT_GRAVEL_SAND = 49.9
MAX_WEIGHT_GRAVEL_SAND = 50.1
MIN_WEIGHT_CEMENT = 24.9
MAX_WEIGHT_CEMENT = 25.1

# Function to check the contents and weight of a single sack
def check_sack(contents, weight):
    # Check contents
    if contents not in ['C', 'G', 'S']:
        return False, "Invalid contents. Accepted values: C, G, S"

    # Check weight based on contents
    if contents == 'C' and not (MIN_WEIGHT_CEMENT < weight < MAX_WEIGHT_CEMENT):
        return False, "Invalid weight for cement sack. Weight should be between 24.9 and 25.1 kilograms"
    elif contents in ['G', 'S'] and not (MIN_WEIGHT_GRAVEL_SAND < weight < MAX_WEIGHT_GRAVEL_SAND):
        return False, "Invalid weight for gravel or sand sack. Weight should be between 49.9 and 50.1 kilograms"

    # If all checks pass, return accepted sack details
    return True, f"{contents} ({weight} kg)"

# Function to check a customer's order for delivery
def check_order(order):
    total_weight = 0
    rejected_sacks = 0

    for sack_type, quantity in order.items():
        for _ in range(quantity):
            contents_input = input(f"Enter contents of the {sack_type} sack (C for cement, G for gravel, S for sand): ").upper()
            weight_input = float(input(f"Enter weight of the {sack_type} sack in kilograms: "))

            # Check the sack using the function from Task 1
            is_accepted, result = check_sack(contents_input, weight_input)

            if is_accepted:
                print(f"{sack_type.capitalize()} sack accepted - {result}")
                total_weight += weight_input
            else:
                print(f"Rejected {sack_type.capitalize()} sack - {result}")
                rejected_sacks += 1

    # Output total weight and number of rejected sacks
    print(f"\nTotal weight of the order: {total_weight} kilograms")
    print(f"Number of rejected sacks: {rejected_sacks}")

# Input data for the customer's order
customer_order = {
    'cement': int(input("Enter the number of cement sacks required: ")),
    'gravel': int(input("Enter the number of gravel sacks required: ")),
    'sand': int(input("Enter the number of sand sacks required: "))
}

# Check and output results for the customer's order
check_order(customer_order)


# In[23]:


#Task-03

MIN_WEIGHT_GRAVEL_SAND = 49.9
MAX_WEIGHT_GRAVEL_SAND = 50.1
MIN_WEIGHT_CEMENT = 24.9
MAX_WEIGHT_CEMENT = 25.1

# Prices for sacks
REGULAR_PRICES = {'C': 3, 'G': 2, 'S': 2}
DISCOUNT_PACK = {'C': 1, 'G': 2, 'S': 2, 'price': 10}

# Function to check the contents and weight of a single sack
def check_sack(contents, weight):
    # Check contents
    if contents not in ['C', 'G', 'S']:
        return False, "Invalid contents. Accepted values: C, G, S"

    # Check weight based on contents
    if contents == 'C' and not (MIN_WEIGHT_CEMENT < weight < MAX_WEIGHT_CEMENT):
        return False, "Invalid weight for cement sack. Weight should be between 24.9 and 25.1 kilograms"
    elif contents in ['G', 'S'] and not (MIN_WEIGHT_GRAVEL_SAND < weight < MAX_WEIGHT_GRAVEL_SAND):
        return False, "Invalid weight for gravel or sand sack. Weight should be between 49.9 and 50.1 kilograms"

    # If all checks pass, return accepted sack details
    return True, f"{contents} ({weight} kg)"

# Function to check a customer's order for delivery and calculate the price
def calculate_price(order):
    total_weight = 0
    rejected_sacks = 0
    regular_price = 0

    for sack_type, quantity in order.items():
        for _ in range(quantity):
            contents_input = input(f"Enter contents of the {sack_type} sack (C for cement, G for gravel, S for sand): ").upper()
            weight_input = float(input(f"Enter weight of the {sack_type} sack in kilograms: "))

            # Check the sack using the function from Task 1
            is_accepted, result = check_sack(contents_input, weight_input)

            if is_accepted:
                print(f"{sack_type.capitalize()} sack accepted - {result}")
                total_weight += weight_input
                regular_price += REGULAR_PRICES[contents_input]
            else:
                print(f"Rejected {sack_type.capitalize()} sack - {result}")
                rejected_sacks += 1

    # Calculate the number of discount packs in the order
    num_discount_packs = min(order.get('cement', 0) // DISCOUNT_PACK['C'],
                             order.get('gravel', 0) // DISCOUNT_PACK['G'],
                             order.get('sand', 0) // DISCOUNT_PACK['S'])

    # Calculate the discount price and amount saved
    discount_price = num_discount_packs * DISCOUNT_PACK['price']
    amount_saved = regular_price - discount_price

    # Output total weight, number of rejected sacks, regular price, and discount information
    print(f"\nTotal weight of the order: {total_weight} kilograms")
    print(f"Number of rejected sacks: {rejected_sacks}")
    print(f"Regular price for the order: ${regular_price}")

    if num_discount_packs > 0:
        print(f"\nDiscount applied: {num_discount_packs} special pack(s)")
        print(f"Discount price for the order: ${discount_price}")
        print(f"Amount saved: ${amount_saved}")
        print(f"New price for the order: ${regular_price - amount_saved + discount_price}")

# Input data for the customer's order
customer_order = {
    'cement': int(input("Enter the number of cement sacks required: ")),
    'gravel': int(input("Enter the number of gravel sacks required: ")),
    'sand': int(input("Enter the number of sand sacks required: "))
}

# Check and output results for the customer's order, including the price calculation
calculate_price(customer_order)


# In[ ]:




