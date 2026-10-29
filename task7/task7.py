
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
member = input("Is customer a member? (yes/no): ").lower()

if quantity <= 0 or price < 0:
    print("Invalid Input")
elif member not in ["yes", "no"]:
    print("Invalid Membership")
else:
    subtotal = quantity * price
    discount1 = 0
    discount2 = 0

    if subtotal >= 5000:
        discount1 = subtotal * 0.10

    amount = subtotal - discount1

    if member == "yes":
        discount2 = amount * 0.05

    amount = amount - discount2
    gst = amount * 0.05
    total = amount + gst

    print("\n--- Retail Bill ---")
    print("Product:", product)
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Purchase Discount: Rs.", round(discount1, 2))
    print("Member Discount: Rs.", round(discount2, 2))
    print("GST: Rs.", round(gst, 2))
    print("Final Bill: Rs.", round(total, 2))
