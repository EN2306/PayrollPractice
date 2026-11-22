import payroll
import pytest

def test_calc_basic_salary():
    assert payroll.calc_basic_salary({"name": "Alice", "department": "IT", "rate": "18.50", "hours": "40"}) == pytest.approx(740.00)
def test_calc_total_payroll():
    assert payroll.calc_total_payroll(payroll.employees) == pytest.approx(3595.00)
def test_get_highest_paid():
    assert payroll.get_highest_paid(payroll.employees) == {'name': 'Charlie', 'department': 'IT', 'rate': '22.00', 'hours': '45'}
def test_get_employees_by_department():
    assert payroll.get_employees_by_department(payroll.employees,"IT") == [{'name': 'Alice', 'department': 'IT', 'rate': '18.50', 'hours': '40'}, {'name': 'Charlie', 'department': 'IT', 'rate': '22.00', 'hours': '45'}]
def test_calc_overtime_pay():
    assert payroll.calc_overtime_pay({"name": "Charlie", "department": "IT", "rate": "22.00", "hours": "45"}) == pytest.approx(55.0)
def test_format_payslip():
    assert payroll.format_payslip({"name": "Alice", "department": "IT", "rate": "18.50", "hours": "40"}) == "Alice (IT) - Basic: $740.00 - Overtime: $0.00"
def test_empty_payroll():
    assert payroll.calc_total_payroll([]) == 0.0
def test_empty_highest():
    assert payroll.get_highest_paid([]) == None
def test_exact_overtime():
    assert payroll.calc_overtime_pay({"name": "Alice", "department": "IT", "rate": "18.50", "hours": "40"}) == 0.0
def test_department_doesnt_exist():
    assert payroll.get_employees_by_department(payroll.employees,"Engineer") == []