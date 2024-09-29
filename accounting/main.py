from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    base_salary = 40000
    bonus = 2000
    overtime = 300

    total_salary = calculate_salary(base_salary, bonus, overtime)
    print("Итоговая заработная плата:", total_salary)

    employees_df = get_employees()
    print(employees_df)


    def current_date():
        """
        Display the current date in DD-MM-YYYY format.
        """
        now = datetime.now()
        return f"Сегодня {now:%d-%m-%Y}"


    print(current_date())