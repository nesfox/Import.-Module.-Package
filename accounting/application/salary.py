def calculate_salary(base_salary, bonus, overtime):
    """
    The function calculates the total salary of an employee, taking into account the base salary, bonus and overtime.
    """

    total_salary = base_salary + bonus + (overtime * 1.5)

    return total_salary
