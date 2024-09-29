import pandas as pd


def get_employees():
    """
    Get a list of company's employees.
    """
    employees = {
        'ID': ['E01', 'E02', 'E03'],
        'Name': ['John Doe', 'Jane Smith', 'Bill Johnson'],
        'Department': ['Sales', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 70000]
    }

    df = pd.DataFrame(employees)
    return df