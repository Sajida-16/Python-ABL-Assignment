
usage = float(input("Enter monthly data usage in GB: "))
budget = float(input("Enter your budget: "))

names = ["Basic", "Standard", "Premium"]
prices = [199, 399, 599]
data = [2, 10, 25]
rates = [50, 30, 20]

if usage < 0 or budget < 0:
    print("Invalid input")
else:
    cheapest = -1
    lowest_cost = float("inf")

    for i in range(3):
        extra = max(0, usage - data[i])
        cost = prices[i] + extra * rates[i]

        print(names[i], "plan cost:", cost)

        if cost <= budget and cost < lowest_cost:
            lowest_cost = cost
            cheapest = i

    if cheapest == -1:
        print("No plan within budget")
    else:
        print("Best plan:", names[cheapest])
        print("Total cost:", lowest_cost)
