
name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
distance = float(input("Enter distance in km: "))
travel_class = input("Enter class (Sleeper/AC): ").lower()

if age < 0 or distance < 0:
    print("Invalid Input")
elif travel_class not in ["sleeper", "ac"]:
    print("Invalid Travel Class")
else:
    if age < 5:
        fare = 0
    elif travel_class == "sleeper":
        fare = distance * 1.5
    else:
        fare = distance * 3

    if age >= 60:
        discount = fare * 0.20
    else:
        discount = 0

    reservation = 40
    total = fare - discount + reservation

    print("\n--- Railway Ticket Details ---")
    print("Passenger Name:", name)
    print("Base Fare: Rs.", round(fare, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Reservation Charge: Rs.", reservation)
    print("Final Fare: Rs.", round(total, 2))
