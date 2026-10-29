
calls = float(input("Enter call minutes: "))
sms = int(input("Enter number of SMS: "))
data = float(input("Enter data usage in GB: "))

if calls < 0 or sms < 0 or data < 0:
    print("Invalid Input")
else:
    a = 99 + calls * 0.8 + sms * 0.5 + data * 20
    b = 199 + calls * 0.5 + sms * 0.3 + data * 10
    c = 299 + calls * 0.2 + sms * 0.1 + data * 5

    print("Plan A Cost: Rs.", round(a, 2))
    print("Plan B Cost: Rs.", round(b, 2))
    print("Plan C Cost: Rs.", round(c, 2))

    if a <= b and a <= c:
        print("Cheapest Plan: Plan A")
    elif b <= a and b <= c:
        print("Cheapest Plan: Plan B")
    else:
        print("Cheapest Plan: Plan C")
