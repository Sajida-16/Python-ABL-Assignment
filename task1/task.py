name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = int(input("Enter subject mark: "))
    marks.append(mark)

attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

total = sum(marks)
percentage = total / 5

if all(0 <= mark <= 100 for mark in marks) and 0 <= attendance <= 100 and income >= 0:
    if percentage >= 85 and min(marks) >= 75 and attendance >= 75 and income <= 250000:
        print("Student:", name)
        print("Percentage:", percentage)
        print("Scholarship Eligible")
    else:
        print("Student:", name)
        print("Percentage:", percentage)
        print("Not Eligible")
else:
    print("Invalid input")
