
units = int(input("Enter units produced: "))
material = float(input("Enter raw material cost: "))
labor = float(input("Enter labor cost: "))
overhead = float(input("Enter overhead cost: "))
price = float(input("Enter selling price per unit: "))

if units <= 0 or material < 0 or labor < 0 or overhead < 0 or price < 0:
    print("Invalid Input")
else:
    cost = material + labor + overhead
    unit_cost = cost / units
    revenue = units * price
    profit = revenue - cost

    print("Total Manufacturing Cost: Rs.", round(cost, 2))
    print("Cost Per Unit: Rs.", round(unit_cost, 2))
    print("Total Revenue: Rs.", round(revenue, 2))

    if profit > 0:
        print("Profit: Rs.", round(profit, 2))
    elif profit < 0:
        print("Loss: Rs.", round(-profit, 2))
    else:
        print("No Profit No Loss")
