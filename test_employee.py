from Employee import employee_details

def test_employee_details_Rahul():
    result = employee_details("Rahul", 101, "IT", 50000)
    expected_result = {
        "Employee Name : Rahul,\n"
        "Employee ID: 101,\n"
        "Department: IT,\n"
        "Salary: 50000"
    }
    assert result == expected_result