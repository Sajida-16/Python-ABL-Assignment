units = float(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 200 + (units - 100) * 3
    else:
        charge = 500 + (units - 200) * 5

    surcharge = charge * 0.05
    total = charge + surcharge + 50

    print("Energy charge:", charge)
    print("Surcharge:", surcharge)
    print("Fixed charge: 50")
    print("Total bill:", total)
