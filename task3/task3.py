diagnosis = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))
payment = float(input("Enter payment amount: "))

if diagnosis < 0 or treatment < 0 or payment < 0:
    print("Invalid input")
else:
    bill = 500 + diagnosis + treatment

    if bill >= 5000:
        bill = bill - bill * 0.10

    balance = bill - payment

    print("Final hospital bill:", round(bill, 2))

    if balance > 0:
        print("Amount due:", round(balance, 2))
    elif balance < 0:
        print("Refund:", round(-balance, 2))
    else:
        print("Payment complete")
