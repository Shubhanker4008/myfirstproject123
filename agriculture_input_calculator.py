# Create an Agriculture Input Cost Calculator.
# Ask the user for:
# Number of bags
# Price per bag
# Calculate total cost

bag=int(input("Enter the number of bags: "))
price= float(input("Enter the price per bag: "))
fertilizer_cost=bag*price
seed_cost=int(input("Enter seed cost: "))
total_cost= fertilizer_cost+seed_cost
print("Fertilizer cost :",fertilizer_cost)
print("Total cost :",total_cost)
