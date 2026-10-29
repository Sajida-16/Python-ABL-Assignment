
participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per participant: "))
sponsor = float(input("Enter sponsorship amount: "))

food = float(input("Enter food expenses: "))
decoration = float(input("Enter decoration expenses: "))
transport = float(input("Enter transportation expenses: "))

registration = participants * fee
income = registration + sponsor
expenses = food + decoration + transport
result = income - expenses

print("\nTotal registration income =", registration)
print("Total income =", income)
print("Total expenses =", expenses)

if result > 0:
    print("Profit =", result)
elif result < 0:
    print("Loss =", -result)
else:
    print("Event has no profit or loss")
