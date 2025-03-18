from abc import ABC, abstractmethod

# Define the abstract Employee class
class Employee(ABC):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

# Define HourlyEmployee subclass
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  # Base salary not used
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Define SalariedEmployee subclass
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)
    
    def calculate_salary(self):
        return self.salary  # Monthly salary

# Example usage
if __name__ == "__main__":
    hourly_emp = HourlyEmployee("H001", "Alice", 20, 160)
    salaried_emp = SalariedEmployee("S001", "Bob", 5000)
    
    print(f"Hourly Employee Salary: {hourly_emp.calculate_salary()}")
    print(f"Salaried Employee Salary: {salaried_emp.calculate_salary()}")
