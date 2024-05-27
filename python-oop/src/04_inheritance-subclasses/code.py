class Employee:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        self.pay = pay
        
    def fullname(self):
        return f"{self.first} {self.last}"
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Developer subclass
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# Manager subclass
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# Example usage
if __name__ == "__main__":
    # Create Developer instances
    dev_1 = Developer('John', 'Doe', 50000, 'Python')
    dev_2 = Developer('Jane', 'Doe', 60000, 'Java')
    
    # Print Developer details
    print(dev_1.email)
    print(dev_1.prog_lang)
    print(dev_2.email)
    print(dev_2.prog_lang)
    
    # Apply raise and print new pay
    dev_1.apply_raise()
    print(dev_1.pay)
    
    # Create Manager instance
    mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
    
    # Print Manager details
    print(mgr_1.email)
    
    # Print employees supervised by Manager
    mgr_1.print_employees()
    
    # Add and remove employees
    mgr_1.add_employee(dev_2)
    mgr_1.print_employees()
    mgr_1.remove_employee(dev_1)
    mgr_1.print_employees()
    
    # Use isinstance and issubclass functions
    print(isinstance(mgr_1, Manager))  # True
    print(isinstance(mgr_1, Employee))  # True
    print(isinstance(mgr_1, Developer))  # False

    print(issubclass(Developer, Employee))  # True
    print(issubclass(Manager, Employee))  # True
    print(issubclass(Manager, Developer))  # False
