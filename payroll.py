
employees = [
    {"name": "Alice", "department": "IT", "rate": "18.50", "hours": "40"},
    {"name": "Bob", "department": "HR", "rate": "16.00", "hours": "35"},
    {"name": "Charlie", "department": "IT", "rate": "22.00", "hours": "45"},
    {"name": "Diana", "department": "Finance", "rate": "20.00", "hours": "42"},
    {"name": "Ethan", "department": "HR", "rate": "15.50", "hours": "30"}
]

def calc_basic_salary(employee):
    if len(employee) == 0:
        return None
    bs = float(employee['rate']) * float(employee['hours'])
    return bs

def calc_total_payroll(employees):
    total = 0.0
    for item in employees:
        total+=float(calc_basic_salary(item))
    return total

def get_highest_paid(employees):
    if len(employees) == 0:
        return None
    a=[]

    for item in employees:
        b=float(calc_basic_salary(item))
        a.append(b)
    h=float(a[0])
    for i in range(len(a)):
        if float(a[i]) > h:
            h=float(a[i])
    for c in range(len(a)):
        if float(a[c]) == float(h):
            return employees[c]

def get_employees_by_department(employees, department):
    e=[]
    for item in employees:
        if item['department'] == department:
            e.append(item)
    return e

def calc_overtime_pay(employee):
    r=0.0
    if float(employee['hours']) <=40:
        return r
    r=(float(employee['hours'])-40)*(float(employee['rate']))*0.5
    return r

def format_payslip(employee):
    return f"{employee['name']} ({employee['department']}) - Basic: ${float(calc_basic_salary(employee)):.2f} - Overtime: ${float(calc_overtime_pay(employee)):.2f}"


def main():
    print("----- Employee Payroll System -----")
    print("1 - Display all employees")
    print("2 - Display total payroll")
    print("3 - Display highest-paid employee")
    print("4 - Display IT employees")
    print("5 - Display payslips")

    s = input("Enter option => ")

    if s == "1":
        for e in employees:
            print(e)

    elif s == "2":
        print(f"${calc_total_payroll(employees):.2f}")

    elif s == "3":
        print(get_highest_paid(employees))

    elif s == "4":
        print(get_employees_by_department(employees, "IT"))

    elif s == "5":
        for e in employees:
            print(format_payslip(e))

if __name__ == "__main__":
    main()
