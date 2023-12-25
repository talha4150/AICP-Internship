#!/usr/bin/env python
# coding: utf-8

# # Talha Ahmad AICP Week-08

# In[15]:


#Task-01


# Constants
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_HOUR = 10
CLOSING_HOUR = 17

# Function to calculate money taken for one boat in a day
def calculate_daily_profit(boat_number):
    print(f"\nBoat {boat_number}:")
    
    # Input start time
    start_hour = int(input("Enter the start hour (between 10 and 16): "))
    
    # Validate start time
    if start_hour < OPENING_HOUR or start_hour >= CLOSING_HOUR:
        print("Error: Invalid start time. Must be between 10 and 16.")
        return
    
    # Input duration
    duration = float(input("Enter the duration (in hours, 0.5 for half an hour): "))
    
    # Validate duration
    if duration <= 0 or start_hour + duration > CLOSING_HOUR:
        print("Error: Invalid duration or return time. Must be greater than 0 and return before 17:00.")
        return
    
    # Calculate cost
    if duration == 0.5:
        cost = HALF_HOUR_RATE
    else:
        cost = HOURLY_RATE * duration
    
    print(f"Amount to be paid: ${cost}")
    
    return cost, duration

# Main program
total_money = 0
total_hours_hired = 0

for boat_num in range(1, 11):
    result = calculate_daily_profit(boat_num)
    
    if result:
        money_taken, hours_hired = result
        total_money += money_taken
        total_hours_hired += hours_hired

# Output at the end of the day
print("\nSummary:")
print(f"Total money taken for the day: ${total_money}")
print(f"Total hours hired for all boats: {total_hours_hired} hours")


# In[16]:


#Task-02

BOAT_COUNT = 10
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_HOUR = 10
CLOSING_HOUR = 17

# Function to calculate money taken for one boat in a day
def calculate_daily_profit(boat_number, current_time):
    print(f"\nBoat {boat_number}:")
    
    # Check if boat is available at the current time
    if boats[boat_number - 1]['return_time'] <= current_time:
        print("This boat is available now!")
        
        # Input start time
        start_hour = int(input("Enter the start hour (between 10 and 16): "))
        
        # Validate start time
        if start_hour < OPENING_HOUR or start_hour >= CLOSING_HOUR:
            print("Error: Invalid start time. Must be between 10 and 16.")
            return
        
        # Input duration
        duration = float(input("Enter the duration (in hours, 0.5 for half an hour): "))
        
        # Validate duration
        if duration <= 0 or start_hour + duration > CLOSING_HOUR:
            print("Error: Invalid duration or return time. Must be greater than 0 and return before 17:00.")
            return
        
        # Calculate cost
        if duration == 0.5:
            cost = HALF_HOUR_RATE
        else:
            cost = HOURLY_RATE * duration
        
        # Update data for the boat
        boats[boat_number - 1]['return_time'] = start_hour + duration
        boats[boat_number - 1]['money_taken'] += cost
        boats[boat_number - 1]['hours_hired'] += duration
        
        print(f"Amount to be paid: ${cost}")
        
        return cost, duration
    else:
        print(f"This boat will be available after {boats[boat_number - 1]['return_time']:.2f} hours.")
        return 0, 0

# Initialize data for each boat
boats = [{'return_time': OPENING_HOUR, 'money_taken': 0, 'hours_hired': 0} for _ in range(BOAT_COUNT)]

# Main program
current_time = float(input("Enter the current time: "))

total_money = 0
total_hours_hired = 0

for boat_num in range(1, BOAT_COUNT + 1):
    result = calculate_daily_profit(boat_num, current_time)
    
    if result:
        money_taken, hours_hired = result
        total_money += money_taken
        total_hours_hired += hours_hired

# Output at the end of the day
print("\nSummary:")
print(f"Total money taken for the day: ${total_money}")
print(f"Total hours hired for all boats: {total_hours_hired} hours")


# In[17]:


#Task-03


# Constants
BOAT_COUNT = 10

# Function to calculate money taken for one boat in a day
def calculate_daily_profit(boat_number):
    print(f"\nBoat {boat_number}:")
    
    # Input start time
    start_hour = int(input("Enter the start hour (between 10 and 16): "))
    
    # Validate start time
    if start_hour < OPENING_HOUR or start_hour >= CLOSING_HOUR:
        print("Error: Invalid start time. Must be between 10 and 16.")
        return
    
    # Input duration
    duration = float(input("Enter the duration (in hours, 0.5 for half an hour): "))
    
    # Validate duration
    if duration <= 0 or start_hour + duration > CLOSING_HOUR:
        print("Error: Invalid duration or return time. Must be greater than 0 and return before 17:00.")
        return
    
    # Calculate cost
    if duration == 0.5:
        cost = HALF_HOUR_RATE
    else:
        cost = HOURLY_RATE * duration
    
    print(f"Amount to be paid: ${cost}")
    
    return cost, duration

# Initialize data for each boat
boats = [{'return_time': OPENING_HOUR, 'money_taken': 0, 'hours_hired': 0} for _ in range(BOAT_COUNT)]

# Main program
total_money = 0
total_hours_hired = 0
unused_boats = 0

for boat_num in range(1, BOAT_COUNT + 1):
    result = calculate_daily_profit(boat_num)
    
    if result:
        money_taken, hours_hired = result
        total_money += money_taken
        total_hours_hired += hours_hired
        if money_taken == 0:  # Boat was not used
            unused_boats += 1

# Find boat used the most
most_used_boat = max(boats, key=lambda x: x['hours_hired'])

# Output at the end of the day
print("\nSummary:")
print(f"Total money taken for the day: ${total_money}")
print(f"Total hours hired for all boats: {total_hours_hired} hours")
print(f"Number of boats not used: {unused_boats}")
print(f"Boat used the most: Boat {boats.index(most_used_boat) + 1} with {most_used_boat['hours_hired']:.2f} hours")


# In[ ]:




