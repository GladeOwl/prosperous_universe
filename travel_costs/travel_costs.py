stl_mrp = 16
ftl_mrp = 24

stl_amount = int(input("STL Fuel amount used: "))
ftl_amount = int(input("FTL Fuel amount used: "))

stl_cost = stl_amount * stl_mrp
ftl_cost = ftl_amount * ftl_mrp

total_cost = stl_cost + ftl_cost

print("\n")
print(f"STL Fuel - \nMarket Price: {stl_mrp} \nAmount: {stl_amount} \nCost: {stl_cost} \n")
print(f"FTL Fuel - \nMarket Price: {ftl_mrp} \nAmount: {ftl_amount} \nCost: {ftl_cost} \n")
print(f"Total Cost of the Journey: {total_cost}")