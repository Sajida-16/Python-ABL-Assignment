
basic = float(input("Enter basic salary: "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive: "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid input")
else:
    hra = basic * 0.20
    allowance = basic * 0.10
    overtime = hours * 100

    gross = basic + hra + allowance + overtime + incentive
    deduction = gross * 0.08
    net = gross - deduction

    print("Basic salary:", basic)
    print("HRA:", hra)
    print("Other allowance:", allowance)
    print("Overtime pay:", overtime)
    print("Gross salary:", round(gross, 2))
    print("Deduction:", round(deduction, 2))
    print("Net salary:", round(net, 2))
