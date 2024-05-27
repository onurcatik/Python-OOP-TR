class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print("Deleting name!")
        self.first_name = None
        self.last_name = None

# Demonstration of functionality
if __name__ == "__main__":
    # Create an Employee instance
    emp = Employee('John', 'Smith')
    
    # Access and print the email and full name
    print(emp.email)       # Output: John.Smith@email.com
    print(emp.full_name)   # Output: John Smith
    
    # Change the first name and print the email and full name again
    emp.first_name = 'Jim'
    print(emp.email)       # Output: Jim.Smith@email.com
    print(emp.full_name)   # Output: Jim Smith
    
    # Set the full name and print the updated first name, last name, and email
    emp.full_name = 'James Bond'
    print(emp.first_name)  # Output: James
    print(emp.last_name)   # Output: Bond
    print(emp.email)       # Output: James.Bond@email.com
    
    # Delete the full name and print the first name and last name
    del emp.full_name
    print(emp.first_name)  # Output: None
    print(emp.last_name)   # Output: None
