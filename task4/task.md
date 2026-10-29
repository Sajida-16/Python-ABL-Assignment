# Problem Statement
Develop a Python program to calculate an employee's gross salary and net salary using basic pay, allowances, overtime hours, and incentives. The program calculates House Rent Allowance (HRA), other allowances, overtime pay, and deductions, then displays the final salary statement.
# Algorithm
1. Start the program.
2. Input basic salary, overtime hours, and incentive amount.
3. Check whether all inputs are non-negative.
4. Calculate HRA as 20% of basic salary.
5. Calculate other allowance as 10% of basic salary.
6. Calculate overtime pay at ₹100 per hour.
7. Calculate gross salary by adding basic salary, HRA, other allowance, overtime pay, and incentive.
8. Calculate deductions as 8% of gross salary.
9. Calculate net salary by subtracting deductions from gross salary.
10. Display the salary details.
11. Stop.
```mermaid
basic = float(input("Enter basic salary: "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive: "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid Input")
else:
    hra = basic * 0.20
    allowance = basic * 0.10
    overtime = hours * 100

    gross = basic + hra + allowance + overtime + incentive
    deduction = gross * 0.08
    net = gross - deduction

    print("HRA: Rs.", hra)
    print("Other Allowance: Rs.", allowance)
    print("Overtime Pay: Rs.", overtime)
    print("Gross Salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net Salary: Rs.", net)
```
# Sample Input
Enter basic salary: 30000
Enter overtime hours: 5
Enter incentive: 2000


# Sample Output
HRA: Rs. 6000.0
Other Allowance: Rs. 3000.0
Overtime Pay: Rs. 500.0
Gross Salary: Rs. 41500.0
Deduction: Rs. 3320.0
Net Salary: Rs. 38180.0


# Calculation
Component	Amount
Basic salary	₹30,000
HRA (20%)	₹6,000
Other allowance (10%)	₹3,000
Overtime pay (5 × ₹100)	₹500
Incentive	₹2,000
Gross salary	₹41,500
Deduction (8%)	₹3,320
Net salary	₹38,180

Result: The employee's gross salary is ₹41,500, and the final net salary after deductions is ₹38,180.

