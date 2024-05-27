import datetime

class Employee:
    # Class variable
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

    # Regular method
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # Class method to set the raise amount
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Class method as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, int(pay))

    # Static method to check if a day is a workday
    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)  # 5 = Saturday, 6 = Sunday

# Example usage
if __name__ == "__main__":
    # Creating instances using the regular constructor
    emp_1 = Employee('John', 'Doe', 70000)
    emp_2 = Employee('Jane', 'Smith', 80000)

    print(emp_1.fullname())
    print(emp_2.fullname())

    # Printing initial raise amount
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)

    # Changing the raise amount using a class method
    Employee.set_raise_amount(1.05)

    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)

    # Creating an instance using the alternative constructor
    emp_str = 'Mike-Jordan-90000'
    new_emp = Employee.from_string(emp_str)
    print(new_emp.fullname())
    print(new_emp.email)

    # Checking if a day is a workday using the static method
    my_date = datetime.date(2023, 5, 15)  # A Monday
    print(Employee.is_workday(my_date))

    my_date = datetime.date(2023, 5, 13)  # A Saturday
    print(Employee.is_workday(my_date))
