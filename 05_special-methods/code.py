class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.first} {self.last} - {self.email}"

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        return len(self.full_name)

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


# Example usage
if __name__ == "__main__":
    emp1 = Employee('John', 'Doe', 50000)
    emp2 = Employee('Jane', 'Smith', 60000)

    print(emp1)              # Calls __str__: John Doe - john.doe@company.com
    print(repr(emp1))        # Calls __repr__: Employee('John', 'Doe', 50000)

    # Demonstrating __add__ method
    print(emp1 + emp2)       # Calls __add__: 110000

    # Demonstrating __len__ method
    print(len(emp1))         # Calls __len__: 8 (length of "John Doe")
