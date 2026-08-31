bag=int(input("Enter the number of bags: "))
price= float(input("Enter the price per bag: "))
fertilizer_cost=bag*price
seed_cost=int(input("Enter seed cost: "))
total_cost= fertilizer_cost+seed_cost
print("The total cost of fertilizer is:", fertilizer_cost)
print("The total cost is:", total_cost)
if total_cost >  10000:
    print("High input cost")
elif total_cost >= 5000:
    print("Medium input cost")
else:
    print("Low input cost")
