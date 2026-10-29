
budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

total = 0

for i in range(n):
    print("\nExpense", i + 1)
    name = input("Enter expense name: ")
    amount = float(input("Enter amount in foreign currency: "))
    rate = float(input("Enter exchange rate in INR: "))

    expense = amount * rate
    total = total + expense

    print(name, "in INR =", round(expense, 2))

print("\nTotal expenses in INR =", round(total, 2))

remaining = budget - total

if remaining >= 0:
    print("Remaining budget in INR =", round(remaining, 2))
    print("Status: Within budget")
else:
    print("Budget exceeded in INR =", round(-remaining, 2))
    print("Status: Over budget")
