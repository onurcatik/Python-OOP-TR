class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Creating instances of the Employee class
employee1 = Employee('Onur', 'Catik', 50000)
employee2 = Employee('Test', 'User', 60000)

# Printing the attributes of the instances
print(f"Employee 1: {employee1.full_name()}, Email: {employee1.email}, Pay: {employee1.pay}")
print(f"Employee 2: {employee2.full_name()}, Email: {employee2.email}, Pay: {employee2.pay}")

# Demonstrating method call using the class name
print(Employee.full_name(employee1))
print(Employee.full_name(employee2))
